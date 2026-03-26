# Scripts Scripts Check Yaml

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_check_yaml.md`
- **Тип**: .MD
- **Размер**: 808 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Check Yaml

- **Путь**: `scripts\scripts\check_yaml.py`
- **Тип**: .PY
- **Размер**: 589 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
# check_yaml.py
import yaml
import sys

try:
    with open('component-config.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    print("✅ YAML успешно загружен!")
    print(f"Версия конфигурации: {data.get('version', 'N/A')}")
    print(f"Название проекта: {data.get('name', 'N/A')}")
except FileNotFoundError:
   
... (файл продолжается)
```

