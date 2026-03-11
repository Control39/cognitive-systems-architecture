# Embedder

- **Путь**: `scripts\python scripts\src\embedding_agent\embedder.py`
- **Тип**: .PY
- **Размер**: 1958 байт
- **Последнее изменение**: 1773162168.1631627

## Предпросмотр

```
import requests
import numpy as np
from typing import List, Optional
import json
from pathlib import Path

class CodeEmbedder:
    def __init__(self, model_name: str = "nomic-embed-text", base_url: str = "http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        
    def embed(self, text: str) -> List[float]:
        """Получить эмбеддинг для текста/кода"""
        try:
            response = requests.post(
                f"{self.base_url}/api/embed
... (файл обрезан для предпросмотра)
```
