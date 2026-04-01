# Generate Obsidian Map

- **Путь**: `07_TOOLS\scripts\generate_obsidian_map.py`
- **Тип**: .PY
- **Размер**: 6,568 байт
- **Последнее изменение**: 2026-03-13 21:11:48

## Превью

```
"""
Генерирует Obsidian-карту знаний из структуры репозитория portfolio-system-architect.
"""

from datetime import datetime
from pathlib import Path
from typing import List, Set
import sys

# Исправляем кодировку для Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Пути
REPO_ROOT: Path = Path(__file__).parent.parent.parent.resolve()  # Поднялись на 3 уровня вверх
OUTPUT_DIR: Path = REPO_ROOT / "docs" / "obsidian-map"
REA
... (файл продолжается)
```


