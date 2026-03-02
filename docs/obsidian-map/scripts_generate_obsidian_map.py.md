# Generate Obsidian Map

- **Путь**: `scripts\generate_obsidian_map.py`
- **Тип**: .PY
- **Размер**: 4957 байт
- **Последнее изменение**: 1771412890.9650793

## Предпросмотр

```
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

# Расширения файлов дл
... (файл обрезан для предпросмотра)
```
