# Test Performance

- **Путь**: `components\ml-model-registry\tests\test_performance.py`
- **Тип**: .PY
- **Размер**: 3465 байт
- **Последнее изменение**: 1772979098.4336722

## Предпросмотр

```
import unittest
import time
from src.core.model_registry import ModelRegistry

class TestModelRegistryPerformance(unittest.TestCase):
    
    def setUp(self):
        self.registry = ModelRegistry()
    
    def test_register_many_models_performance(self):
        """Проверка производительности при регистрации множества моделей"""
        start_time = time.time()
        
        # Регистрация 1000 моделей
        for i in range(1000):
            model_data = {
                "name": f"Model 
... (файл обрезан для предпросмотра)
```
