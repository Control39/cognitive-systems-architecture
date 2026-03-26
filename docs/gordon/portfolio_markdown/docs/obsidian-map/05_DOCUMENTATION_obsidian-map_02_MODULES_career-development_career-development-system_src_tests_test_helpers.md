# 02 Modules Career Development Career Development System Src Tests Test Helpers

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_career-development_career-development-system_src_tests_test_helpers.md`
- **Тип**: .MD
- **Размер**: 843 байт
- **Последнее изменение**: 2026-03-13 20:21:32

## Превью

```
# Test Helpers

- **Путь**: `02_MODULES\career-development\career-development-system\src\tests\test_helpers.py`
- **Тип**: .PY
- **Размер**: 5,628 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import unittest
import os
import tempfile
from src.utils.helpers import *


class TestHelpers(unittest.TestCase):

    def test_validate_email(self):
        """Тест валидации email"""
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("
... (файл продолжается)
```

