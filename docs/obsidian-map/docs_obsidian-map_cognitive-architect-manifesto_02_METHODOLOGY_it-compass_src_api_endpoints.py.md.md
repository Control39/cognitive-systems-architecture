# Cognitive Architect Manifesto 02 Methodology It Compass Src Api Endpoints.Py

- **Путь**: `docs\obsidian-map\cognitive-architect-manifesto_02_METHODOLOGY_it-compass_src_api_endpoints.py.md`
- **Тип**: .MD
- **Размер**: 853 байт
- **Последнее изменение**: 1772467524.0443258

## Предпросмотр

```
# Endpoints

- **Путь**: `cognitive-architect-manifesto\02_METHODOLOGY\it-compass\src\api\endpoints.py`
- **Тип**: .PY
- **Размер**: 985 байт
- **Последнее изменение**: 1772460530.9804976

## Предпросмотр

```
from fastapi import APIRouter, Depends
from src.core.tracker import CompetencyTracker

router = APIRouter(prefix="/api/v1", tags=["competencies"])

@router.get("/skills/{skill_id}/markers")
async def get_markers(skill_id: str, tracker: CompetencyTracker = Depends()):
    return tracker.get
... (файл обрезан для предпросмотра)
```
