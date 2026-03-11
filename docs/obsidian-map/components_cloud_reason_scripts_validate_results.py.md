# Validate Results

- **Путь**: `components\cloud_reason\scripts\validate_results.py`
- **Тип**: .PY
- **Размер**: 10740 байт
- **Последнее изменение**: 1772979098.3521364

## Предпросмотр

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка корректности конвертации файлов в UTF-8.
Валидирует, что все файлы действительно в UTF-8 и читаются без ошибок.
"""
import os
import chardet
import logging
from pathlib import Path
import json
from typing import Dict, List, Tuple
import unicodedata

def setup_logging() -> None:
    """Настройка системы логирования"""
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
   
... (файл обрезан для предпросмотра)
```
