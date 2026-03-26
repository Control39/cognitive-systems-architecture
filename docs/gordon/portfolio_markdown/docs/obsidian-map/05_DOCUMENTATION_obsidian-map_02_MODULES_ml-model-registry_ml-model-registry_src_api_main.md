# 02 Modules Ml Model Registry Ml Model Registry Src Api Main

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_src_api_main.md`
- **Тип**: .MD
- **Размер**: 804 байт
- **Последнее изменение**: 2026-03-13 20:21:31

## Превью

```
# Main

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\src\api\main.py`
- **Тип**: .PY
- **Размер**: 571 байт
- **Последнее изменение**: 2026-03-10 19:02:48

## Превью

```
from fastapi import FastAPI
from portfolio_integration import router as portfolio_router

app = FastAPI(title="ML Model Registry API", version="0.1.0")

app.include_router(portfolio_router)

@app.get("/")
async def root():
    return {"message": "ML Model Registry API"}

@app.get("/health")
async def health():
  
... (файл продолжается)
```

