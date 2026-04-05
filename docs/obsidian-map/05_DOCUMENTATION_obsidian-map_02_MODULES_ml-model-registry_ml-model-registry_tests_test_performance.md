# 02 Modules Ml Model Registry Ml Model Registry Tests Test Performance

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_performance.md`
- **Тип**: .MD
- **Размер**: 899 байт
- **Последнее изменение**: 2026-03-13 20:21:37

## Превью

```
# Test Performance

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_performance.py`
- **Тип**: .PY
- **Размер**: 3,465 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import unittest
import time
from src.core.model_registry import ModelRegistry

class TestModelRegistryPerformance(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_many_models_performance(self):
        """Проверка производител
... (файл продолжается)
```


