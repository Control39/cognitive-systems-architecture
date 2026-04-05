# 02 Modules Ml Model Registry Ml Model Registry Tests Test Resilience

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_resilience.md`
- **Тип**: .MD
- **Размер**: 880 байт
- **Последнее изменение**: 2026-03-13 20:21:31

## Превью

```
# Test Resilience

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_resilience.py`
- **Тип**: .PY
- **Размер**: 1,159 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```

import unittest
from unittest.mock import patch, MagicMock
from src.core.model_registry import ModelRegistry
from src.storage.model_storage import ModelStorage

class TestModelRegistryResilience(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    d
... (файл продолжается)
```


