# Components Ml Model Registry Tests Test Edge Cases.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_edge_cases.py.md`
- **Тип**: .MD
- **Размер**: 911 байт
- **Последнее изменение**: 1772467523.923321

## Предпросмотр

```
# Test Edge Cases

- **Путь**: `components\ml-model-registry\tests\test_edge_cases.py`
- **Тип**: .PY
- **Размер**: 3184 байт
- **Последнее изменение**: 1772457556.512181

## Предпросмотр

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistryEdgeCases(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_model_with_none_data(self):
        """Проверка регистрации модели с None вместо данных"""
   
... (файл обрезан для предпросмотра)
```
