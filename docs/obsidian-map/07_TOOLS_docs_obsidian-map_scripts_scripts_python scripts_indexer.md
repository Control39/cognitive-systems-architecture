# Scripts Scripts Python Scripts Indexer

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_python scripts_indexer.md`
- **Тип**: .MD
- **Размер**: 818 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Indexer

- **Путь**: `scripts\scripts\python scripts\indexer.py`
- **Тип**: .PY
- **Размер**: 5,838 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
import ast
from pathlib import Path
from typing import List, Dict, Any
import json
from .embedder import CodeEmbedder

class CodeIndexer:
    def __init__(self, embedder: CodeEmbedder, chunk_size: int = 1000):
        self.embedder = embedder
        self.chunk_size = chunk_size
        self.index = []
        
    def chunk_pyt
... (файл продолжается)
```


