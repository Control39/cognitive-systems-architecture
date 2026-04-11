#!/usr/bin/env python3
"""
Collector Script for Cognitive Systems Architecture
Gathers scattered notes, dialogs, and code snippets from local paths and SourceCraft repos.
Integrates them into the main repo for RAG indexing and portfolio generation.

Usage:
    python scripts/collector.py --local-paths /path/to/notes /path/to/dialogs --sourcecraft-repo https://github.com/user/repo
"""

import json
import shutil
import argparse
import hashlib
import git
from pathlib import Path

class Collector:
    ALLOWED_SUFFIXES = [".md", ".txt", ".py", ".json"]

    def __init__(self, output_dir="docs/notes"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def collect_local(self, paths):
        """Collect files from local paths."""
        for path in paths:
            src_path = Path(path)
            if src_path.exists():
                for file in src_path.rglob("*"):
                    if file.is_file() and file.suffix in self.ALLOWED_SUFFIXES:
                        rel_path = file.relative_to(src_path)
                        dest = self.output_dir / rel_path
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(file, dest)
                        print(f"Copied: {file} -> {dest}")
            else:
                print(f"Path not found: {path}")

    def collect_sourcecraft(self, repo_url, branch="main"):
        """Clone and integrate SourceCraft repo."""
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        clone_dir = self.output_dir / "sourcecraft" / repo_name
        if clone_dir.exists():
            shutil.rmtree(clone_dir)
        git.Repo.clone_from(repo_url, clone_dir, branch=branch)
        print(f"Cloned SourceCraft repo: {repo_url} -> {clone_dir}")

    def deduplicate(self):
        """Remove duplicates based on content hash."""
        seen_hashes = {}
        duplicates = []

        files = sorted(
            [p for p in self.output_dir.rglob("*") if p.is_file() and p.suffix in self.ALLOWED_SUFFIXES]
        )

        for file_path in files:
            file_hash = self._hash_file(file_path)
            if file_hash in seen_hashes:
                duplicates.append(file_path)
                file_path.unlink()
                print(f"Removed duplicate: {file_path}")
            else:
                seen_hashes[file_hash] = file_path

        return duplicates

    def index_for_rag(self):
        """Prepare files for RAG indexing."""
        index = {
            "generated_from": str(self.output_dir),
            "files": []
        }

        files = sorted(
            [p for p in self.output_dir.rglob("*") if p.is_file() and p.suffix in self.ALLOWED_SUFFIXES]
        )

        for file_path in files:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            index["files"].append({
                "path": str(file_path.relative_to(self.output_dir)),
                "size": file_path.stat().st_size,
                "sha256": self._hash_file(file_path),
                "lines": content.count("\n") + 1 if content else 0,
            })

        index_path = self.output_dir / "index.json"
        index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Generated RAG index: {index_path}")
        return index_path

    def _hash_file(self, file_path):
        hasher = hashlib.sha256()
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect and integrate scattered artifacts.")
    parser.add_argument("--local-paths", nargs="+", help="Local paths to scan")
    parser.add_argument("--sourcecraft-repo", help="SourceCraft repo URL")
    args = parser.parse_args()

    collector = Collector()
    if args.local_paths:
        collector.collect_local(args.local_paths)
    if args.sourcecraft_repo:
        collector.collect_sourcecraft(args.sourcecraft_repo)
    collector.deduplicate()
    collector.index_for_rag()