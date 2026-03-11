# Low Energy Mode

- **Путь**: `components\it-compass\src\core\low_energy_mode.py`
- **Тип**: .PY
- **Размер**: 5881 байт
- **Последнее изменение**: 1773162168.1448178

## Предпросмотр

```
"""
Режим низкой энергии для IT Compass (обновлённая версия)
Использует объединённый модуль PsychologicalSupport для обеспечения функциональности.
Обеспечивает обратную совместимость с предыдущими версиями.
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import logging

# Импортируем PsychologicalSupport из core.mental
try:
    from .mental.psychological_support import PsychologicalSupport
except ImportError:
    # Fallback для случ
... (файл обрезан для предпросмотра)
```
