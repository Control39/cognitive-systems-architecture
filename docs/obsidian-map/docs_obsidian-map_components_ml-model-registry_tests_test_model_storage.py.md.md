# Components Ml Model Registry Tests Test Model Storage.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_tests_test_model_storage.py.md`
- **Тип**: .MD
- **Размер**: 904 байт
- **Последнее изменение**: 1772467523.9293234

## Предпросмотр

```
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
        self.test_dir = tempfile.mkd
... (файл обрезан для предпросмотра)
```
