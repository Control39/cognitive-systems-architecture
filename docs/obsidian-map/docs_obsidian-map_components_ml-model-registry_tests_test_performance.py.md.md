# Components Ml Model Registry Tests Test Performance.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_performance.py.md`
- **Тип**: .MD
- **Размер**: 915 байт
- **Последнее изменение**: 1772680654.9071653

## Предпросмотр

```
# Test Performance

- **Путь**: `components\ml-model-registry\tests\test_performance.py`
- **Тип**: .PY
- **Размер**: 3382 байт
- **Последнее изменение**: 1772457970.7464614

## Предпросмотр

```
import unittest
import time
from src.core.model_registry import ModelRegistry

class TestModelRegistryPerformance(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_many_models_performance(self):
        """Проверка производительности при рег
... (файл обрезан для предпросмотра)
```
