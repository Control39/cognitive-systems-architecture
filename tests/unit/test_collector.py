import json
from pathlib import Path
from scripts.collector import Collector


def test_deduplicate_removes_duplicate_files(tmp_path):
    output_dir = tmp_path / "docs" / "notes"
    collector = Collector(output_dir=output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    file1 = output_dir / "file1.md"
    file2 = output_dir / "file2.md"
    file3 = output_dir / "file3.md"

    file1.write_text("hello world", encoding="utf-8")
    file2.write_text("hello world", encoding="utf-8")
    file3.write_text("another file", encoding="utf-8")

    duplicates = collector.deduplicate()

    assert file1.exists()
    assert not file2.exists()
    assert file3.exists()
    assert len(duplicates) == 1
    assert duplicates[0] == file2


def test_index_for_rag_generates_json_index(tmp_path):
    output_dir = tmp_path / "docs" / "notes"
    collector = Collector(output_dir=output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "a.md").write_text("first line\nsecond line", encoding="utf-8")
    (output_dir / "b.txt").write_text("only one line", encoding="utf-8")

    index_path = collector.index_for_rag()

    assert index_path.exists()
    index_data = json.loads(index_path.read_text(encoding="utf-8"))
    assert index_data["generated_from"] == str(output_dir)
    assert len(index_data["files"]) == 2
    paths = {item["path"] for item in index_data["files"]}
    assert paths == {"a.md", "b.txt"}
    assert any(item["lines"] == 2 for item in index_data["files"])
    assert any(item["lines"] == 1 for item in index_data["files"])


def test_collect_local_copies_supported_files(tmp_path):
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "note.md").write_text("note", encoding="utf-8")
    (source_dir / "script.py").write_text("print(1)", encoding="utf-8")
    (source_dir / "ignore.bin").write_bytes(b"binary")

    output_dir = tmp_path / "docs" / "notes"
    collector = Collector(output_dir=output_dir)

    collector.collect_local([str(source_dir)])

    assert (output_dir / "note.md").exists()
    assert (output_dir / "script.py").exists()
    assert not (output_dir / "ignore.bin").exists()
