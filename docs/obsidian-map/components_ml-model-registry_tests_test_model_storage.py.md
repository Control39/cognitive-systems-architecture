# Test Model Storage

- **Путь**: `components\ml-model-registry\tests\test_model_storage.py`
- **Тип**: .PY
- **Размер**: 2752 байт
- **Последнее изменение**: 1772457881.6691103

## Предпросмотр

```
import unittest
import os
import tempfile
import json
from src.storage.model_storage import ModelStorage

class TestModelStorage(unittest.TestCase):
    
    def setUp(self):
        self.storage = ModelStorage()
        # Создание временной директории для тестов
        self.test_dir = tempfile.mkdtemp()
        self.storage.storage_path = self.test_dir
    
    def tearDown(self):
        # Очистка временных файлов
        for file in os.listdir(self.test_dir):
            os.remove(os.path.jo
... (файл обрезан для предпросмотра)
```
