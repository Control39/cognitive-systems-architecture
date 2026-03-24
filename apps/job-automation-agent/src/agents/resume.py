from jinja2 import Environment, FileSystemLoader
from typing import Dict
import os

# Загрузка шаблона резюме (создадим templates/resume.md.j2)
template_dir = os.path.join(os.path.dirname(__file__), \"../../templates\")
env = Environment(loader=FileSystemLoader(template_dir), 
                  block_start_string=\"[%\", block_end_string=\"%]\")

async def generate_resume(user_profile: Dict, job_desc: Dict) -> str:
    \"\"\"Генерирует Markdown/HTML резюме под вакансию.\"\"\" 
    try:
        template = env.get_template(\"resume.md.j2\")
        tailored_content = template.render(
            user=user_profile,
            job=job_desc,
            highlighted_skills=[s for s in user_profile[\"skills\"] 
                               if any(kw in job_desc[\"description\"].lower() 
                                      for kw in s.lower().split())]
        )
        return tailored_content
    except Exception as e:
        return f\"Error generating resume: {str(e)}\"

def resume_tool(job_title: str, skills: str) -> str:
    \"\"\"LangChain tool stub.\"\"\" 
    profile = {\"name\": \"Your Name\", \"skills\": skills.split(\", \"), \"experience\": \"5+ years\"}
    job = {\"title\": job_title, \"description\": \"Python dev needed\"}
    result = asyncio.run(generate_resume(profile, job))
    return result[:500] + \"...\"  # truncate

if __name__ == \"__main__\": 
    import asyncio
    print(asyncio.run(generate_resume({}, {})))

