# 02 Modules Cloud Reason Cloud Reason Core Module Loader

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_cloud-reason_cloud_reason_core_module-loader.md`
- **Тип**: .MD
- **Размер**: 838 байт
- **Последнее изменение**: 2026-03-13 20:21:46

## Превью

```
# Module Loader

- **Путь**: `02_MODULES\cloud-reason\cloud_reason\core\module-loader.py`
- **Тип**: .PY
- **Размер**: 908 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import importlib.util
from pathlib import Path
from ..config.loader import COMPONENT_CONFIG

def load_module_by_name(module_name):
    """Загружает Python‑модуль по имени из конфигурации."""
    for module_info in COMPONENT_CONFIG["modules"]:
        if module_info["name"] == module_name:
            module_
... (файл продолжается)
```


