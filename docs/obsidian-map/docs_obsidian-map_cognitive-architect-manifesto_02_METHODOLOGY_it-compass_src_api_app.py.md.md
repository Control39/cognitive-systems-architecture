# Cognitive Architect Manifesto 02 Methodology It Compass Src Api App.Py

- **Путь**: `docs\obsidian-map\cognitive-architect-manifesto_02_METHODOLOGY_it-compass_src_api_app.py.md`
- **Тип**: .MD
- **Размер**: 649 байт
- **Последнее изменение**: 1772467524.0433223

## Предпросмотр

```
# App

- **Путь**: `cognitive-architect-manifesto\02_METHODOLOGY\it-compass\src\api\app.py`
- **Тип**: .PY
- **Размер**: 387 байт
- **Последнее изменение**: 1772460623.8874817

## Предпросмотр

```
from fastapi import FastAPI
from src.api.endpoints import router
from src.infrastructure.monitoring.metrics import setup_metrics
from src.utils.logger import setup_logging

app = FastAPI(title="IT-Compass API", version="0.1.0")

# Подключаем роутеры
app.include_router(router)

# Метрики и логирование

... (файл обрезан для предпросмотра)
```
