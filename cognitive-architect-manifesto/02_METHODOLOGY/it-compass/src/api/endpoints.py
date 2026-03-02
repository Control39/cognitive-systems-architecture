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

@app.get("/api/visualizations/skill-radar")
async def get_skill_radar(user_id: str):
    """Данные для radar chart навыков"""
    tracker = CompetencyTracker(user_id)
    return {
        "labels": ["Python", "PowerShell", "System Design", "AI Integration"],
        "values": [0.75, 0.60, 0.45, 0.80],
        "max_value": 1.0
    }

@app.get("/health")
async def health():
    return {"status": "ok", "service": "it-compass", "version": "0.1.0"}