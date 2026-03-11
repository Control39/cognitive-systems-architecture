# Endpoints

- **Путь**: `components\cloud_reason\api\endpoints.py`
- **Тип**: .PY
- **Размер**: 1890 байт
- **Последнее изменение**: 1772979098.3369987

## Предпросмотр

```
# components/cloud-reason/api/endpoints.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ..config.loader import COMPONENT_CONFIG
from ..config.utils import get_module_path, find_endpoint_by_path

app = FastAPI(
    title=COMPONENT_CONFIG["component"]["name"],
    version=COMPONENT_CONFIG["component"]["version"],
    description=COMPONENT_CONFIG["component"]["description"]
)

class ReasoningRequest(BaseModel):
    context_sources: list
    query: str
    reasoning
... (файл обрезан для предпросмотра)
```
