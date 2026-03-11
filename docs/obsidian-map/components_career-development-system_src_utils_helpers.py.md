# Helpers

- **Путь**: `components\career-development-system\src\utils\helpers.py`
- **Тип**: .PY
- **Размер**: 3268 байт
- **Последнее изменение**: 1772979098.333997

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
        return None
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filepath}")
        return None


def save_json_file(filepath, data):
    """Сохранить данные
... (файл обрезан для предпросмотра)
```
