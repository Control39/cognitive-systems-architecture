# Scripts Scripts Python Scripts Src Embedding Agent Search Demo

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_python scripts_src_embedding_agent_search_demo.md`
- **Тип**: .MD
- **Размер**: 956 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Search Demo

- **Путь**: `scripts\scripts\python scripts\src\embedding_agent\search_demo.py`
- **Тип**: .PY
- **Размер**: 4,106 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
#!/usr/bin/env python
import sys
from pathlib import Path
import json
import numpy as np

# Добавляем путь к src
sys.path.append(str(Path(__file__).parent.parent))

from src.embedding_agent.embedder import CodeEmbedder

def load_full_index(index_file: str):
    """Загружает полный индекс с эмбеддингам
... (файл продолжается)
```

