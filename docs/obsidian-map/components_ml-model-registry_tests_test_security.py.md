# Test Security

- **Путь**: `components\ml-model-registry\tests\test_security.py`
- **Тип**: .PY
- **Размер**: 3767 байт
- **Последнее изменение**: 1772979098.4357004

## Предпросмотр

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistrySecurity(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_model_id_injection_attempt(self):
        """Проверка попытки инъекции через ID модели"""
        # Попытка инъекции через ID модели
        malicious_id = "test_model'; DROP TABLE models; --"
        model_data = {"name": "Test Model", "version": "1.0"}
        
        result = self.registry.re
... (файл обрезан для предпросмотра)
```
