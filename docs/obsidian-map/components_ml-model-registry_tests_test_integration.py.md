# Test Integration

- **Путь**: `components\ml-model-registry\tests\test_integration.py`
- **Тип**: .PY
- **Размер**: 4768 байт
- **Последнее изменение**: 1772457588.4375253

## Предпросмотр

```
import unittest
import os
import tempfile
import json
from src.core.model_registry import ModelRegistry
from src.storage.model_storage import ModelStorage

class TestModelRegistryIntegration(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
        self.storage = ModelStorage()
        # Создание временной директории для тестов
        self.test_dir = tempfile.mkdtemp()
        self.storage.storage_path = self.test_dir
    
    def tearDown(self):
        # Оч
... (файл обрезан для предпросмотра)
```
