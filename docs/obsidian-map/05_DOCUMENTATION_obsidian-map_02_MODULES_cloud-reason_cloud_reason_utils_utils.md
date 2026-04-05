# 02 Modules Cloud Reason Cloud Reason Utils Utils

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_cloud-reason_cloud_reason_utils_utils.md`
- **Тип**: .MD
- **Размер**: 869 байт
- **Последнее изменение**: 2026-03-13 20:21:29

## Превью

```
# Utils

- **Путь**: `02_MODULES\cloud-reason\cloud_reason\utils\utils.py`
- **Тип**: .PY
- **Размер**: 1,146 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
# components/cloud-reason/config/utils.py
from .loader import COMPONENT_CONFIG

def get_module_path(module_name):
    """Возвращает путь к модулю по его имени."""
    for module in COMPONENT_CONFIG["modules"]:
        if module["name"] == module_name:
            return module["path"]
    raise ValueError(f"Модуль {modul
... (файл продолжается)
```


