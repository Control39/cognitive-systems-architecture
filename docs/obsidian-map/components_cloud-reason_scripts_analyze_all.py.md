# Analyze All

- **Путь**: `components\cloud-reason\scripts\analyze_all.py`
- **Тип**: .PY
- **Размер**: 6492 байт
- **Последнее изменение**: 1771412428.9454062

## Предпросмотр

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Анализ всех текстовых файлов в проекте на предмет кодировки.
Поддерживает кириллицу в путях и названиях файлов.
"""
import os
import chardet
import logging
from pathlib import Path
import json
from typing import Dict, List, Tuple

def setup_logging() -> None:
    """Настройка системы логирования"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            loggi
... (файл обрезан для предпросмотра)
```
