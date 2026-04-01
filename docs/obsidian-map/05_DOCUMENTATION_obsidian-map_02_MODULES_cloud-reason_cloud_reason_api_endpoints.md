# 02 Modules Cloud Reason Cloud Reason Api Endpoints

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_cloud-reason_cloud_reason_api_endpoints.md`
- **Тип**: .MD
- **Размер**: 798 байт
- **Последнее изменение**: 2026-03-13 20:21:46

## Превью

```
# Endpoints

- **Путь**: `02_MODULES\cloud-reason\cloud_reason\api\endpoints.py`
- **Тип**: .PY
- **Размер**: 1,890 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
# components/cloud-reason/api/endpoints.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ..config.loader import COMPONENT_CONFIG
from ..config.utils import get_module_path, find_endpoint_by_path

app = FastAPI(
    title=COMPONENT_CONFIG["component"]["name"],
    version=COMPONENT_C
... (файл продолжается)
```


