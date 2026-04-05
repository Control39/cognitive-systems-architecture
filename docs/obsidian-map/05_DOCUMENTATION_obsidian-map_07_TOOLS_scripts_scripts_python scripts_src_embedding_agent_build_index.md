# 07 Tools Scripts Scripts Python Scripts Src Embedding Agent Build Index

- **Путь**: `05_DOCUMENTATION\obsidian-map\07_TOOLS_scripts_scripts_python scripts_src_embedding_agent_build_index.md`
- **Тип**: .MD
- **Размер**: 923 байт
- **Последнее изменение**: 2026-03-13 20:21:38

## Превью

```
# Build Index

- **Путь**: `07_TOOLS\scripts\scripts\python scripts\src\embedding_agent\build_index.py`
- **Тип**: .PY
- **Размер**: 1,442 байт
- **Последнее изменение**: 2026-03-10 19:02:48

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
    print("🚀 Начинаем индексацию кодовой
... (файл продолжается)
```


