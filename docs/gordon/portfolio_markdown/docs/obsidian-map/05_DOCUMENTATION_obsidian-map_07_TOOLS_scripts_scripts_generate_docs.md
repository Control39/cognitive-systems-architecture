# 07 Tools Scripts Scripts Generate Docs

- **Путь**: `05_DOCUMENTATION\obsidian-map\07_TOOLS_scripts_scripts_generate_docs.md`
- **Тип**: .MD
- **Размер**: 844 байт
- **Последнее изменение**: 2026-03-13 20:21:40

## Превью

```
# Generate Docs

- **Путь**: `07_TOOLS\scripts\scripts\generate_docs.py`
- **Тип**: .PY
- **Размер**: 1,039 байт
- **Последнее изменение**: 2026-03-05 05:17:36

## Превью

```
from ..config.loader import COMPONENT_CONFIG

def generate_api_docs():
    """Генерирует документацию API на основе конфигурации."""
    docs = f"# {COMPONENT_CONFIG['component']['name']}\n\n"
    docs += f"**Версия:** {COMPONENT_CONFIG['component']['version']}\n\n"
    docs += "## Эндпоинты\n\n"

    for endpoint in COMPO
... (файл продолжается)
```

