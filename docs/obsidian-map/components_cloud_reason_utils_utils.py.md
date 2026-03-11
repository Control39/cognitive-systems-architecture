# Utils

- **Путь**: `components\cloud_reason\utils\utils.py`
- **Тип**: .PY
- **Размер**: 1146 байт
- **Последнее изменение**: 1772979098.359262

## Предпросмотр

```
# components/cloud-reason/config/utils.py
from .loader import COMPONENT_CONFIG

def get_module_path(module_name):
    """Возвращает путь к модулю по его имени."""
    for module in COMPONENT_CONFIG["modules"]:
        if module["name"] == module_name:
            return module["path"]
    raise ValueError(f"Модуль {module_name} не найден в конфигурации")

def find_endpoint_by_path(path):
    """Находит эндпоинт по пути."""
    for endpoint in COMPONENT_CONFIG["endpoints"]:
        if endpoint["p
... (файл обрезан для предпросмотра)
```
