# Components Ml Model Registry Tests Test Contract.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_contract.py.md`
- **Тип**: .MD
- **Размер**: 911 байт
- **Последнее изменение**: 1772680654.8904843

## Предпросмотр

```
# Test Contract

- **Путь**: `components\ml-model-registry\tests\test_contract.py`
- **Тип**: .PY
- **Размер**: 7973 байт
- **Последнее изменение**: 1772458399.9811027

## Предпросмотр

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistryContract(unittest.TestCase):
    """Контрактные тесты для проверки совместимости интерфейсов"""
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_model_contract(self):
        "
... (файл обрезан для предпросмотра)
```
