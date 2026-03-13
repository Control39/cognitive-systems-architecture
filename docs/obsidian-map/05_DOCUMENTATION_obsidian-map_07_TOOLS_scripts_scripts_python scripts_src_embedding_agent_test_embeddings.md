# 07 Tools Scripts Scripts Python Scripts Src Embedding Agent Test Embeddings

- **Путь**: `05_DOCUMENTATION\obsidian-map\07_TOOLS_scripts_scripts_python scripts_src_embedding_agent_test_embeddings.md`
- **Тип**: .MD
- **Размер**: 921 байт
- **Последнее изменение**: 2026-03-13 20:21:29

## Превью

```
# Test Embeddings

- **Путь**: `07_TOOLS\scripts\scripts\python scripts\src\embedding_agent\test_embeddings.py`
- **Тип**: .PY
- **Размер**: 1,035 байт
- **Последнее изменение**: 2026-03-10 19:02:48

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
        ("def hello(): prin
... (файл продолжается)
```

