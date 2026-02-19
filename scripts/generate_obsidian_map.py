"""
Генерирует Obsidian-карту знаний из структуры репозитория portfolio-system-architect.
С полной аннотацией типов.
"""

import os
from pathlib import Path
from typing import List, Set

# Пути
REPO_ROOT: Path = Path(".")
OUTPUT_DIR: Path = Path("docs/obsidian-map")
README_PATH: Path = Path("README.md")

# Игнорируемые директории
IGNORED_DIRS: Set[str] = {
    ".git", "__pycache__", "node_modules", "venv", "env", 
    ".vscode", ".idea", ".gigaide", "backups", ".backup"
}

# Расширения файлов для включения
INCLUDE_EXTENSIONS: Set[str] = {".md", ".py", ".ps1", ".sh", ".yaml", ".yml", ".json", ".toml"}


def get_all_files(root: Path) -> List[Path]:
    """Получает все файлы в директории рекурсивно, исключая игнорируемые."""
    files: List[Path] = []
    for item in root.rglob("*"):
        if item.is_file():
            # Проверяем, не находится ли файл в игнорируемой директории
            if not any(ignored in item.parts for ignored in IGNORED_DIRS):
                # Проверяем расширение
                if item.suffix.lower() in INCLUDE_EXTENSIONS:
                    files.append(item)
    return files


def generate_note_content(file_path: Path) -> str:
    """Генерирует содержимое заметки для файла."""
    relative_path: Path = file_path.relative_to(REPO_ROOT)
    
    # Определяем тип файла
    suffix: str = file_path.suffix.lower()
    
    # Заголовок
    title: str = relative_path.stem.replace("-", " ").replace("_", " ").title()
    
    # Содержание заметки
    content: str = f"# {title}\n\n"
    content += f"- **Путь**: `{relative_path}`\n"
    content += f"- **Тип**: {suffix.upper() if suffix else 'Файл'}\n"
    content += f"- **Размер**: {file_path.stat().st_size} байт\n"
    content += f"- **Последнее изменение**: {file_path.stat().st_mtime}\n\n"
    
    # Для текстовых файлов добавляем предпросмотр
    if suffix in {".md", ".py", ".ps1", ".sh", ".yaml", ".yml", ".json", ".toml"}:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                file_content: str = f.read()
            content += "## Предпросмотр\n\n"
            content += "```\n"
            # Ограничиваем предпросмотр 500 символами
            preview: str = file_content[:500]
            content += preview
            if len(file_content) > 500:
                content += "\n... (файл обрезан для предпросмотра)"
            content += "\n```\n"
        except Exception as e:
            content += f"## Ошибка чтения\n\nНе удалось прочитать файл: {e}\n"
    
    return content


def main() -> None:
    """Основная функция генерации карты знаний."""
    # Создаем директорию для вывода
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Получаем все файлы
    files: List[Path] = get_all_files(REPO_ROOT)
    
    # Генерируем заметки
    file: Path
    for file in files:
        try:
            # Генерируем имя заметки (относительный путь с заменой / на _)
            note_name: str = str(file.relative_to(REPO_ROOT)).replace(os.sep, "_")
            note_path: Path = OUTPUT_DIR / f"{note_name}.md"
            
            # Генерируем содержимое заметки
            content: str = generate_note_content(file)
            
            # Записываем заметку
            with open(note_path, "w", encoding="utf-8") as f:
                f.write(content)
            
            print(f"[OK] Создана заметка: {note_name}.md")
        except Exception as e:
            print(f"[X] Ошибка при создании заметки для {file}: {e}")
    
    # Создаем главную заметку README
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            readme_content: str = f.read()
        
        main_note_path: Path = OUTPUT_DIR / "README.md"
        with open(main_note_path, "w", encoding="utf-8") as f:
            f.write("# Главная\n\n")
            f.write(readme_content)
        
        print("[OK] Создана главная заметка README.md")
    except Exception as e:
        print(f"[X] Ошибка при создании главной заметки: {e}")
    
    print(f"[V] Карта знаний Obsidian сгенерирована в: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()