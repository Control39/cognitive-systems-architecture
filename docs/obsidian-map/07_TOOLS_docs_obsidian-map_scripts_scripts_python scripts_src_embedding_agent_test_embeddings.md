# Scripts Scripts Python Scripts Src Embedding Agent Test Embeddings

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_python scripts_src_embedding_agent_test_embeddings.md`
- **Тип**: .MD
- **Размер**: 914 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Test Embeddings

- **Путь**: `scripts\scripts\python scripts\src\embedding_agent\test_embeddings.py`
- **Тип**: .PY
- **Размер**: 1,035 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.embedding_agent.embedder import CodeEmbedder

def test_embedder():
    """Тестирование работы эмбеддера"""
    embedder = CodeEmbedder()
    
    test_cases = [
        ("def hello(): print('world'
... (файл продолжается)
```

