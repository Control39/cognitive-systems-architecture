# 02 Modules Ml Model Registry Ml Model Registry Tests Test Model Registry

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_model_registry.md`
- **Тип**: .MD
- **Размер**: 829 байт
- **Последнее изменение**: 2026-03-13 20:21:29

## Превью

```
# Test Model Registry

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_model_registry.py`
- **Тип**: .PY
- **Размер**: 4,627 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistry(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_model(self):
        result = self.registry.register_model("test_model", {"name"
... (файл продолжается)
```


