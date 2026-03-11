# Components Career Development System Src Tests Test Helpers.Py

- **Путь**: `docs\obsidian-map\components_career-development-system_src_tests_test_helpers.py.md`
- **Тип**: .MD
- **Размер**: 858 байт
- **Последнее изменение**: 1772680654.8410428

## Предпросмотр

```
# Test Helpers

- **Путь**: `components\career-development-system\src\tests\test_helpers.py`
- **Тип**: .PY
- **Размер**: 5628 байт
- **Последнее изменение**: 1771483370.8604653

## Предпросмотр

```
import unittest
import os
import tempfile
from src.utils.helpers import *


class TestHelpers(unittest.TestCase):

    def test_validate_email(self):
        """Тест валидации email"""
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name@domai
... (файл обрезан для предпросмотра)
```
