# 07 Tools Scripts Scripts Check Yaml

- **Путь**: `05_DOCUMENTATION\obsidian-map\07_TOOLS_scripts_scripts_check_yaml.md`
- **Тип**: .MD
- **Размер**: 815 байт
- **Последнее изменение**: 2026-03-13 20:21:35

## Превью

```
# Check Yaml

- **Путь**: `07_TOOLS\scripts\scripts\check_yaml.py`
- **Тип**: .PY
- **Размер**: 589 байт
- **Последнее изменение**: 2026-03-10 19:02:48

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
except FileNotFoundE
... (файл продолжается)
```


