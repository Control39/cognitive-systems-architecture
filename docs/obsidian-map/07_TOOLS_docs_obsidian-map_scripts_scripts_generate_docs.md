# Scripts Scripts Generate Docs

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_generate_docs.md`
- **Тип**: .MD
- **Размер**: 837 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Generate Docs

- **Путь**: `scripts\scripts\generate_docs.py`
- **Тип**: .PY
- **Размер**: 1,039 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
from ..config.loader import COMPONENT_CONFIG

def generate_api_docs():
    """Генерирует документацию API на основе конфигурации."""
    docs = f"# {COMPONENT_CONFIG['component']['name']}\n\n"
    docs += f"**Версия:** {COMPONENT_CONFIG['component']['version']}\n\n"
    docs += "## Эндпоинты\n\n"

    for endpoint in COMPONENT_CONF
... (файл продолжается)
```


