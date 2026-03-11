# Loader

- **Путь**: `components\cloud_reason\configs\loader.py`
- **Тип**: .PY
- **Размер**: 857 байт
- **Последнее изменение**: 1772979098.3399742

## Предпросмотр

```
# components/cloud-reason/config/loader.py
import yaml
from pathlib import Path

def load_component_config():
    """Загружает конфигурацию компонента из component-config.yaml в корне проекта."""
    project_root = Path(__file__).parent.parent.parent
    config_path = project_root / "component-config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
         
... (файл обрезан для предпросмотра)
```
