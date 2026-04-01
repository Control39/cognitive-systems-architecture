# Scripts Scripts Python Scripts Src Embedding Agent Build Index

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_python scripts_src_embedding_agent_build_index.md`
- **Тип**: .MD
- **Размер**: 916 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Build Index

- **Путь**: `scripts\scripts\python scripts\src\embedding_agent\build_index.py`
- **Тип**: .PY
- **Размер**: 1,442 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
#!/usr/bin/env python
import sys
from pathlib import Path

# Добавляем путь к src
sys.path.append(str(Path(__file__).parent.parent))

from src.embedding_agent.embedder import CodeEmbedder
from src.embedding_agent.indexer import CodeIndexer

def main():
    print("🚀 Начинаем индексацию кодовой базы..."
... (файл продолжается)
```


