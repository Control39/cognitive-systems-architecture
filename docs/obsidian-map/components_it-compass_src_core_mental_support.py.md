# Mental Support

- **Путь**: `components\it-compass\src\core\mental_support.py`
- **Тип**: .PY
- **Размер**: 7229 байт
- **Последнее изменение**: 1773162168.1468165

## Предпросмотр

```
"""
Психологическая поддержка для IT Compass (совместимость с предыдущими версиями)
Обеспечивает интерфейс MentalSupport, MoodRecord, SelfHelpPractices,
используя объединённый модуль PsychologicalSupport.
"""

import json
import random
from datetime import datetime, date
from typing import Dict, List, Optional, Any
from .mental.psychological_support import PsychologicalSupport as PS


class MoodRecord:
    """Запись психологического состояния пользователя"""
    
    def __init__(
        self,

... (файл обрезан для предпросмотра)
```
