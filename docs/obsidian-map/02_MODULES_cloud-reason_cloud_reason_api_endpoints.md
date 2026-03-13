# Endpoints

- **Путь**: `02_MODULES\cloud-reason\cloud_reason\api\endpoints.py`
- **Тип**: .PY
- **Размер**: 1,938 байт
- **Последнее изменение**: 2026-03-13 20:23:58

## Превью

```
# components/cloud-reason/api/endpoints.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ..config.loader import COMPONENT_CONFIG
from ..config.utils import get_module_path, find_endpoint_by_path

app = FastAPI(
    title=COMPONENT_CONFIG["component"]["name"],
    version=COMPONENT_CONFIG["component"]["version"],
    description=COMPONENT_CONFIG["component"]["description"],
    docs_url="/docs",
    redoc_url="/redoc"
)

class ReasoningRequest(BaseModel):
    cont
... (файл продолжается)
```

