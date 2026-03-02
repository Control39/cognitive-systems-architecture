# Api Integration

- **Путь**: `components\it-compass.bak\src\core\api_integration.py`
- **Тип**: .PY
- **Размер**: 23816 байт
- **Последнее изменение**: 1771215256.9148352

## Предпросмотр

```
"""
Модуль интеграции с внешними API для IT Compass.

Этот модуль предоставляет классы и функции для интеграции с внешними
платформами, такими как GitHub, Coursera, LinkedIn и другими.
"""

import json
import requests
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod
import os


@dataclass
class UserActivity:
    """
    Активность пользователя на внешней платформе.
    """
    platform: str             # Платформа (github,
... (файл обрезан для предпросмотра)
```
