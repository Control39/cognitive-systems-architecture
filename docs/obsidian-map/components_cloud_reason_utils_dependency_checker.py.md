# Dependency Checker

- **Путь**: `components\cloud_reason\utils\dependency_checker.py`
- **Тип**: .PY
- **Размер**: 1690 байт
- **Последнее изменение**: 1772979098.3582609

## Предпросмотр

```
# components/cloud-reason/utils/dependency_checker.py
import pkg_resources
import subprocess
import sys
from ..config.loader import COMPONENT_CONFIG
from ..config.utils import get_env_variables

def check_dependencies():
    """Проверяет установленные зависимости против требований конфигурации."""
    required = COMPONENT_CONFIG["dependencies"]["python"]
    missing = []

    for requirement in required:
        try:
            pkg_resources.require(requirement)
        except pkg_resources.Dis
... (файл обрезан для предпросмотра)
```
