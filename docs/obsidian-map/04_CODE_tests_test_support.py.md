# Test Support

- **Путь**: `04_CODE\tests\test_support.py`
- **Тип**: .PY
- **Размер**: 4150 байт
- **Последнее изменение**: 1773162168.0759692

## Предпросмотр

```
"""
Тесты для модуля психологической поддержки.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.mental.support import PsychologicalSupport
import pytest
from unittest.mock import patch, MagicMock

def test_psychological_support_initialization():
    """Проверяем, что класс инициализируется без ошибок."""
    ps = PsychologicalSupport()
    assert ps is not None
    assert hasattr(ps, 'motivational_quotes')
    assert hasa
... (файл обрезан для предпросмотра)
```
