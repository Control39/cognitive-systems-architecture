# Test Cli

- **Путь**: `04_CODE\tests\test_cli.py`
- **Тип**: .PY
- **Размер**: 5062 байт
- **Последнее изменение**: 1773162168.0749714

## Предпросмотр

```
"""
Тесты для CLI интерфейса IT Compass.
"""
import sys
import os
import pytest
from unittest.mock import patch, MagicMock, call
import builtins

# Добавляем путь к модулям
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Импортируем модули
try:
    from core.tracker import SkillTracker
    from cli.main import main, show_menu, show_directions, show_markers_for_direction, mark_marker_completed, show_progress, generate_portfolio
except ImportError as e:
... (файл обрезан для предпросмотра)
```
