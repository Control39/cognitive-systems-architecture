# Components Ml Model Registry Src Api Main.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_src_api_main.py.md`
- **Тип**: .MD
- **Размер**: 513 байт
- **Последнее изменение**: 1772467523.939323

## Предпросмотр

```
# Main

- **Путь**: `components\ml-model-registry\src\api\main.py`
- **Тип**: .PY
- **Размер**: 266 байт
- **Последнее изменение**: 1772453836.9888606

## Предпросмотр

```
from fastapi import FastAPI

app = FastAPI(title="ML Model Registry API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "ML Model Registry API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```
