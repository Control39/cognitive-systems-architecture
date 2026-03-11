# App

- **Путь**: `components\it-compass\src\ui\app.py`
- **Тип**: .PY
- **Размер**: 14345 байт
- **Последнее изменение**: 1773162168.1488166

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
from ..core.mental.psychological_support import PsychologicalSupport as PS


class ITCompassApp:
    """Осно
... (файл обрезан для предпросмотра)
```
