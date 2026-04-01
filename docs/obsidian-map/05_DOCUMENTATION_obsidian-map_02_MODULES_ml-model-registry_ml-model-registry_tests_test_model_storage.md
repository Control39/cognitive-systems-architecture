# 02 Modules Ml Model Registry Ml Model Registry Tests Test Model Storage

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_tests_test_model_storage.md`
- **Тип**: .MD
- **Размер**: 888 байт
- **Последнее изменение**: 2026-03-13 20:21:28

## Превью

```
# Test Model Storage

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\tests\test_model_storage.py`
- **Тип**: .PY
- **Размер**: 2,816 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

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
        self.test_dir 
... (файл продолжается)
```


