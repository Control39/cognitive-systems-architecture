# Test Model Registry

- **Путь**: `components\ml-model-registry\tests\test_model_registry.py`
- **Тип**: .PY
- **Размер**: 4627 байт
- **Последнее изменение**: 1772979098.4326732

## Предпросмотр

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistry(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_model(self):
        result = self.registry.register_model("test_model", {"name": "Test Model"})
        self.assertEqual(result["status"], "success")
    
    def test_get_model(self):
        self.registry.register_model("test_model", {"name": "Test Model"})
        result = self.registry.get_
... (файл обрезан для предпросмотра)
```
