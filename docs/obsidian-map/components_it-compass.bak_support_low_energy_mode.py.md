# Low Energy Mode

- **Путь**: `components\it-compass.bak\support\low_energy_mode.py`
- **Тип**: .PY
- **Размер**: 13940 байт
- **Последнее изменение**: 1771212952.2894754

## Предпросмотр

```
"""
Режим низкой энергии для IT Compass
Поддержка пользователей в периоды низкой мотивации и энергии
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging


class LowEnergyMode:
    """Режим поддержки в периоды низкой энергии"""
    
    def __init__(self):
        """Инициализация режима низкой энергии"""
        self.logger = logging.getLogger(__name__)
        self.motivational_quotes = self._load_motivational_quotes()
 
... (файл обрезан для предпросмотра)
```
