# Marker Export

- **Путь**: `components\it-compass\src\utils\marker_export.py`
- **Тип**: .PY
- **Размер**: 10698 байт
- **Последнее изменение**: 1772450580.823584

## Предпросмотр

```
"""
Модуль экспорта маркеров для интеграции с LLM и RAG-системами.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any
from ..core.tracker import CareerTracker, Marker

logger = logging.getLogger(__name__)


class MarkerExporter:
    """Класс для экспорта маркеров в различные форматы для LLM и RAG-поиска."""

    def __init__(self, tracker: CareerTracker):
        self.tracker = tracker

    def export_to_llm_format(self, output_path: str) -> bool:
       
... (файл обрезан для предпросмотра)
```
