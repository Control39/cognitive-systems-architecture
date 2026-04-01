# 02 Modules Ml Model Registry Ml Model Registry Tests Test Integration

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_integration.md`
- **Тип**: .MD
- **Размер**: 864 байт
- **Последнее изменение**: 2026-03-13 20:21:33

## Превью

```
# Test Integration

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_integration.py`
- **Тип**: .PY
- **Размер**: 4,883 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

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
        self.
... (файл продолжается)
```


