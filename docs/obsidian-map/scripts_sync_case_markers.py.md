# Sync Case Markers

- **Путь**: `scripts\sync_case_markers.py`
- **Тип**: .PY
- **Размер**: 9144 байт
- **Последнее изменение**: 1772448919.108977

## Предпросмотр

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скрипт автоматической синхронизации кейса с IT-Compass
Автоматизирует процесс интеграции кейсов с маркерами IT-Compass
"""

import json
import logging
import os
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class ITCompassSync:
    def __init__(
        self,
        case_path: str,
        it_compass_path: str = "components/it-compass",
        portfolio_path: str = "components/portfol
... (файл обрезан для предпросмотра)
```
