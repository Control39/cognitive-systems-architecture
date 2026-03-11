# Main

- **Путь**: `components\it-compass.bak\src\main.py`
- **Тип**: .PY
- **Размер**: 7429 байт
- **Последнее изменение**: 1771211934.103954

## Предпросмотр

```
"""
IT Compass - система объективного отслеживания карьерного роста в IT
Основное консольное приложение
"""

import os
import sys
from core.tracker import SkillTracker
from utils.portfolio_gen import PortfolioGenerator


def show_directions(tracker):
    """Показать список направлений"""
    directions = tracker.get_directions()
    print("\n🎯 Доступные направления:")
    for i, direction in enumerate(directions, 1):
        print(f"{i}. {direction}")


def show_markers_for_direction(tracker, di
... (файл обрезан для предпросмотра)
```
