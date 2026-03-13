# Scripts Scripts Python Scripts Search Code

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_python scripts_search_code.md`
- **Тип**: .MD
- **Размер**: 814 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Search Code

- **Путь**: `scripts\scripts\python scripts\search_code.py`
- **Тип**: .PY
- **Размер**: 1,527 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
import json
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_embedding(text):
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )
    return respo
... (файл продолжается)
```

