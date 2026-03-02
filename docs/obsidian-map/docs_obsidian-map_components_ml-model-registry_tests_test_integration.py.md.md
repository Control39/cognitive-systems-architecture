# Components Ml Model Registry Tests Test Integration.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_integration.py.md`
- **Тип**: .MD
- **Размер**: 880 байт
- **Последнее изменение**: 1772467523.926324

## Предпросмотр

```
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
        self.storage = Mode
... (файл обрезан для предпросмотра)
```
