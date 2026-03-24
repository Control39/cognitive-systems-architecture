import pandas as pd
from typing import List, Dict
from apps.career-development.src.src.core.db import get_db  # Shared career DB
import asyncio

async def analyze_career_progress(user_id: str) -> Dict:
    \"\"\"Analysis Agent: Метрики из career DB + job data.\"\"\" 
    async for session in get_db():
        # Stub query (real: skills progress, applications)
        skills_df = pd.DataFrame({
            \"skill\": [\"Python\", \"FastAPI\", \"PostgreSQL\"],
            \"level\": [4, 3, 4],
            \"progress\": [80, 60, 90]
        })
    
    trends = {
        \"avg_level\": skills_df[\"level\"].mean(),
        \"top_skills\": skills_df.nlargest(3, \"progress\")[\"skill\"].tolist(),
        \"recommendations\": [\"Улучшить DevOps\", \"Добавить Kubernetes\"],
        \"market_trends\": \"Python devs: +20% demand (stub from hh.ru stats)\"
    }
    return trends

def analysis_tool(jobs: str, applications: int) -> str:
    \"\"\"LangChain tool.\"\"\" 
    df = pd.read_json(jobs) if jobs else pd.DataFrame()
    return f\"Trends: {len(df)} jobs, {applications} apps. {str(await analyze_career_progress('user1'))}\"

if __name__ == \"__main__\": 
    import asyncio
    print(asyncio.run(analyze_career_progress(\"user1\")))

