# Test Tracker

- **Путь**: `components\it-compass\tests\test_tracker.py`
- **Тип**: .PY
- **Размер**: 12010 байт
- **Последнее изменение**: 1772800980.8182454

## Предпросмотр

```
"""
Тесты для трекера компетенций IT Compass
"""

import unittest
import json
import os
import tempfile
import sys
from datetime import datetime
from unittest.mock import patch, mock_open

# Добавляем путь к модулям IT Compass
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.core.tracker import CompetencyTracker


class TestCompetencyTracker(unittest.TestCase):
    """Тесты для трекера компетенций"""
    
    def setUp(self):
        """Настройка перед каждым те
... (файл обрезан для предпросмотра)
```
