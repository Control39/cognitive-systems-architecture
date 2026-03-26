# 02 Modules Ml Model Registry Ml Model Registry Tests Test Edge Cases

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_edge_cases.md`
- **Тип**: .MD
- **Размер**: 896 байт
- **Последнее изменение**: 2026-03-13 20:21:32

## Превью

```
# Test Edge Cases

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_edge_cases.py`
- **Тип**: .PY
- **Размер**: 3,248 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
import unittest
from src.core.model_registry import ModelRegistry

class TestModelRegistryEdgeCases(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_model_with_none_data(self):
        """Проверка регистрации модели с None вмест
... (файл продолжается)
```

