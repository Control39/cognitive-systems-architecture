# 02 Modules Cloud Reason Cloud Reason Configs Loader

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_cloud-reason_cloud_reason_configs_loader.md`
- **Тип**: .MD
- **Размер**: 863 байт
- **Последнее изменение**: 2026-03-13 20:21:40

## Превью

```
# Loader

- **Путь**: `02_MODULES\cloud-reason\cloud_reason\configs\loader.py`
- **Тип**: .PY
- **Размер**: 857 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
# components/cloud-reason/config/loader.py
import yaml
from pathlib import Path

def load_component_config():
    """Загружает конфигурацию компонента из component-config.yaml в корне проекта."""
    project_root = Path(__file__).parent.parent.parent
    config_path = project_root / "component-config.yaml"

    if not 
... (файл продолжается)
```


