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
    return tracker.get_markers_for_skill(skill_id)

@router.post("/progress")
async def update_progress(marker_id: str, status: str):
    tracker = CompetencyTracker()
    return tracker.update_marker_status(marker_id, status)

@app
... (файл обрезан для предпросмотра)
```
