# 04 Code Tests Test Cli

- **Путь**: `05_DOCUMENTATION\obsidian-map\04_CODE_tests_test_cli.md`
- **Тип**: .MD
- **Размер**: 826 байт
- **Последнее изменение**: 2026-03-13 20:21:30

## Превью

```
# Test Cli

- **Путь**: `04_CODE\tests\test_cli.py`
- **Тип**: .PY
- **Размер**: 5,062 байт
- **Последнее изменение**: 2026-03-10 19:02:48

## Превью

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
    from cli.
... (файл продолжается)
```

