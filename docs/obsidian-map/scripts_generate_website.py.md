# Generate Website

- **Путь**: `scripts\generate_website.py`
- **Тип**: .PY
- **Размер**: 7675 байт
- **Последнее изменение**: 1771412836.7699783

## Предпросмотр

```
"""
Генерирует профессиональный сайт-портфолио с поддержкой Mermaid и Git-статуса.
С полной аннотацией типов.
"""

import os
from pathlib import Path
import markdown as md
from typing import List, Tuple, Dict

INPUT_DIR: Path = Path("docs/obsidian-map")
OUTPUT_DIR: Path = Path("docs/website")
LOGO_PATH: str = "assets/logo.svg"


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{title} — portfolio-system-architect</title>
    <meta name="viewport" c
... (файл обрезан для предпросмотра)
```
