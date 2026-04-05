# Generate Website

- **Путь**: `07_TOOLS\docs\obsidian-map\generate_website.md`
- **Тип**: .MD
- **Размер**: 858 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Generate Website

- **Путь**: `generate_website.py`
- **Тип**: .PY
- **Размер**: 7,890 байт
- **Последнее изменение**: 2026-03-13 20:24:02

## Превью

```
"""
Генерирует профессиональный сайт-портфолио с поддержкой Mermaid и Git-статуса.
"""

import subprocess
from pathlib import Path
import markdown as md
from typing import List, Tuple, Dict

# Пути
REPO_ROOT: Path = Path(__file__).parent.parent.resolve()
OUTPUT_DIR: Path = REPO_ROOT / "docs" / "website"
LOGO_PATH: str = REPO_ROOT / "assets" 
... (файл продолжается)
```


