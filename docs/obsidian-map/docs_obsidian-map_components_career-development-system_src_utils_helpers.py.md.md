# Components Career Development System Src Utils Helpers.Py

- **Путь**: `docs\obsidian-map\components_career-development-system_src_utils_helpers.py.md`
- **Тип**: .MD
- **Размер**: 912 байт
- **Последнее изменение**: 1772680654.8410428

## Предпросмотр

```
# Helpers

- **Путь**: `components\career-development-system\src\utils\helpers.py`
- **Тип**: .PY
- **Размер**: 3268 байт
- **Последнее изменение**: 1771483370.8292177

## Предпросмотр

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
        print(f"Файл {filepath} не найден")
       
... (файл обрезан для предпросмотра)
```
