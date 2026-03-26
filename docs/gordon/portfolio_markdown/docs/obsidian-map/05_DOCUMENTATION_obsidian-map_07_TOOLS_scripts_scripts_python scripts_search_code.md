# 07 Tools Scripts Scripts Python Scripts Search Code

- **Путь**: `05_DOCUMENTATION\obsidian-map\07_TOOLS_scripts_scripts_python scripts_search_code.md`
- **Тип**: .MD
- **Размер**: 821 байт
- **Последнее изменение**: 2026-03-13 20:21:39

## Превью

```
# Search Code

- **Путь**: `07_TOOLS\scripts\scripts\python scripts\search_code.py`
- **Тип**: .PY
- **Размер**: 1,527 байт
- **Последнее изменение**: 2026-03-10 19:02:48

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
    ret
... (файл продолжается)
```

