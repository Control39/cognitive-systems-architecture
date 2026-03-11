# Components Ml Model Registry Tests Test Security.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_security.py.md`
- **Тип**: .MD
- **Размер**: 893 байт
- **Последнее изменение**: 1772680654.9071653

## Предпросмотр

```
# Test Security

- **Путь**: `components\ml-model-registry\tests\test_security.py`
- **Тип**: .PY
- **Размер**: 3686 байт
- **Последнее изменение**: 1772458004.6408956

## Предпросмотр

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistrySecurity(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_model_id_injection_attempt(self):
        """Проверка попытки инъекции через ID модели"""
        # Попытка
... (файл обрезан для предпросмотра)
```
