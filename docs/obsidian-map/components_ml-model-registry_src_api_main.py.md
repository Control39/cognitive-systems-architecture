# Main

- **Путь**: `components\ml-model-registry\src\api\main.py`
- **Тип**: .PY
- **Размер**: 571 байт
- **Последнее изменение**: 1773162168.1508167

## Предпросмотр

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
    return {"status": "healthy", "service": "ml-model-registry"}
@app.get("/")
async def root():
    return {"message": "ML Model Registry API"}

if __name__ == "__main__":
    import uvic
... (файл обрезан для предпросмотра)
```
