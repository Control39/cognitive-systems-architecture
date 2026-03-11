# Portfolio Gen

- **Путь**: `components\it-compass.bak\src\utils\portfolio_gen.py`
- **Тип**: .PY
- **Размер**: 21233 байт
- **Последнее изменение**: 1771212883.5313828

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
