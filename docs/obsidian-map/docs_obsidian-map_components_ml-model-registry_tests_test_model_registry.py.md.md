# Components Ml Model Registry Tests Test Model Registry.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_model_registry.py.md`
- **Тип**: .MD
- **Размер**: 845 байт
- **Последнее изменение**: 1772680654.8904843

## Предпросмотр

```
# Test Model Registry

- **Путь**: `components\ml-model-registry\tests\test_model_registry.py`
- **Тип**: .PY
- **Размер**: 4525 байт
- **Последнее изменение**: 1772457151.6335764

## Предпросмотр

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistry(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_model(self):
        result = self.registry.register_model("test_model", {"name": "Test Model"
... (файл обрезан для предпросмотра)
```
