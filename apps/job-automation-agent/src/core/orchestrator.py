import asyncio
from typing import Dict, Any
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Настройка LLM (замените YOUR_API_KEY)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="YOUR_OPENAI_API_KEY",  # Установите env OPENAI_API_KEY
    temperature=0.1
)

# Инструменты-агенты (stubs, расширим)
def job_search(query: str) -> str:
    \"\"\"Ищет вакансии на hh.ru.\"\"\" 
    return f\"Найдено 5 вакансий по '{query}' на hh.ru (stub - добавим парсер).\"

def generate_resume(job_title: str, user_skills: str) -> str:
    \"\"\"Генерирует персонализированное резюме.\"\"\" 
    return f\"Резюме для {job_title}: Подчеркнуты skills {user_skills} (stub - Jinja2+LLM).\"

from ..agents.analysis import analysis_tool 
def analyze_progress(jobs_data: str, applications: int) -> str:
    \"\"\"Анализирует прогресс карьеры.\"\"\" 
    return analysis_tool(jobs_data, applications)

tools = [
    Tool(
        name=\"JobSearchAgent\",
        func=job_search,
        description=\"Поиск вакансий по ключевым словам (query: str) -> list вакансий.\"
    ),
    Tool(
        name=\"ResumeAgent\",
        func=generate_resume,
        description=\"Генерация резюме для вакансии (job_title, user_skills).\"
    ),
    Tool(
        name=\"AnalysisAgent\",
        func=analyze_progress,
        description=\"Анализ карьеры (jobs_data, applications_count).\"
    )
]

# ReAct Prompt для Core Agent
prompt = PromptTemplate.from_template(
    \"\"\"Ты Core Agent - координатор карьеры. 
    Задача: {input}
    Используй агенты по порядку: JobSearch -> Resume -> Analysis. 
    Контекст: {{context}}
    Мысли шаг за шагом, затем действуй.
    {agent_scratchpad}\"\"\"
)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

async def run_core_agent(task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    \"\"\"Запуск Core Agent (async wrapper).\"\"\" 
    if context is None:
        context = {}
    
    try:
        result = agent_executor.invoke({
            \"input\": task,
            \"context\": str(context)
        })
        return {
            \"success\": True,
            \"output\": result[\"output\"],
            \"intermediate_steps\": result.get(\"intermediate_steps\", [])
        }
    except Exception as e:
        return {\"success\": False, \"error\": str(e)}

if __name__ == \"__main__\": 
    async def demo():
        result = await run_core_agent(\"Найди вакансии Python developer и подготовь резюме.\")
        print(result)
    
    asyncio.run(demo())

