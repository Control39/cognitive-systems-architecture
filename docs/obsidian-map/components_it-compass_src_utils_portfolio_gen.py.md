# Portfolio Gen

- **Путь**: `components\it-compass\src\utils\portfolio_gen.py`
- **Тип**: .PY
- **Размер**: 21845 байт
- **Последнее изменение**: 1772680654.6223345

## Предпросмотр

```
"""
Генератор портфолио для IT Compass
Утилита для автоматической генерации профессионального портфолио
на основе прогресса пользователя
"""

import json
import os
import shutil
from datetime import datetime
from typing import Dict, List, Optional
from jinja2 import Environment, FileSystemLoader


class PortfolioGenerator:
    """Генератор профессионального портфолио"""
    
    def __init__(self, template_dir: str = "templates", output_dir: str = "portfolio"):
        """
        Инициализация 
... (файл обрезан для предпросмотра)
```
