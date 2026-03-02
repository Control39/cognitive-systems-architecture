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
    
    def test_register_model_with_storage_failure(self):
        """Проверка регистрации модели при сбое хранилища"""
        # Регистрация модели
        model_data = {"name": "Test Model", "version": "1.0"}
     
... (файл обрезан для предпросмотра)
```
