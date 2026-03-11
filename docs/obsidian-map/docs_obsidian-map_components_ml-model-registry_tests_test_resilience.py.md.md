# Components Ml Model Registry Tests Test Resilience.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_resilience.py.md`
- **Тип**: .MD
- **Размер**: 896 байт
- **Последнее изменение**: 1772680654.9071653

## Предпросмотр

```
# Test Resilience

- **Путь**: `components\ml-model-registry\tests\test_resilience.py`
- **Тип**: .PY
- **Размер**: 1135 байт
- **Последнее изменение**: 1772458196.0444887

## Предпросмотр

```

import unittest
from unittest.mock import patch, MagicMock
from src.core.model_registry import ModelRegistry
from src.storage.model_storage import ModelStorage

class TestModelRegistryResilience(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_regist
... (файл обрезан для предпросмотра)
```
