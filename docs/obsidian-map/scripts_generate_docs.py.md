# Generate Docs

- **Путь**: `scripts\generate_docs.py`
- **Тип**: .PY
- **Размер**: 1039 байт
- **Последнее изменение**: 1772680656.0232306

## Предпросмотр

```
from ..config.loader import COMPONENT_CONFIG

def generate_api_docs():
    """Генерирует документацию API на основе конфигурации."""
    docs = f"# {COMPONENT_CONFIG['component']['name']}\n\n"
    docs += f"**Версия:** {COMPONENT_CONFIG['component']['version']}\n\n"
    docs += "## Эндпоинты\n\n"

    for endpoint in COMPONENT_CONFIG["endpoints"]:
        docs += f"### {endpoint['method']} {endpoint['path']}\n"
        docs += f"{endpoint['description']}\n\n"

        if "parameters" in endpoint
... (файл обрезан для предпросмотра)
```
