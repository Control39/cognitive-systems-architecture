# Module Loader

- **Путь**: `components\cloud_reason\core\module-loader.py`
- **Тип**: .PY
- **Размер**: 908 байт
- **Последнее изменение**: 1772979098.3431394

## Предпросмотр

```
import importlib.util
from pathlib import Path
from ..config.loader import COMPONENT_CONFIG

def load_module_by_name(module_name):
    """Загружает Python‑модуль по имени из конфигурации."""
    for module_info in COMPONENT_CONFIG["modules"]:
        if module_info["name"] == module_name:
            module_path = Path(__file__).parent.parent / module_info["path"]
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_s
... (файл обрезан для предпросмотра)
```
