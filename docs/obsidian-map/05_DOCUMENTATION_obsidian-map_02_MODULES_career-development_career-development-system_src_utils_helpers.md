# 02 Modules Career Development Career Development System Src Utils Helpers

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_career-development_career-development-system_src_utils_helpers.md`
- **Тип**: .MD
- **Размер**: 897 байт
- **Последнее изменение**: 2026-03-13 20:21:49

## Превью

```
# Helpers

- **Путь**: `02_MODULES\career-development\career-development-system\src\utils\helpers.py`
- **Тип**: .PY
- **Размер**: 3,268 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import json
import os
from datetime import datetime


def load_json_file(filepath):
    """Загрузить данные из JSON файла"""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filepath} не н
... (файл продолжается)
```


