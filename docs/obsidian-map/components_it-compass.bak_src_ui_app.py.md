# App

- **Путь**: `components\it-compass.bak\src\ui\app.py`
- **Тип**: .PY
- **Размер**: 13919 байт
- **Последнее изменение**: 1771212656.3657255

## Предпросмотр

```
"""
Веб-интерфейс для IT Compass
Основное приложение с веб-интерфейсом для отслеживания навыков
"""

import streamlit as st
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

# Импортируем модули из проекта
from ..core.tracker import SkillTracker
from ..core.api_integration import APIIntegration
from ..utils.portfolio_gen import PortfolioGenerator
from ..support.low_energy_mode import LowEnergyMode


class ITCompassApp:
    """Основной класс веб-приложен
... (файл обрезан для предпросмотра)
```
