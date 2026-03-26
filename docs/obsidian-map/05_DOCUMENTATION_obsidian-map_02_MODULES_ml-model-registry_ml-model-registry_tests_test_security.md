# 02 Modules Ml Model Registry Ml Model Registry Tests Test Security

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_security.md`
- **Тип**: .MD
- **Размер**: 877 байт
- **Последнее изменение**: 2026-03-13 20:21:31

## Превью

```
# Test Security

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_security.py`
- **Тип**: .PY
- **Размер**: 3,767 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistrySecurity(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_model_id_injection_attempt(self):
        """Проверка попытки инъекции через ID модели"""
   
... (файл продолжается)
```

