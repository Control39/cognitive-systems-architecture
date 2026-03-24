import requests
from bs4 import BeautifulSoup
from typing import List, Dict

async def search_hh_ru(query: str, area: str = \"1\") -> List[Dict]:
    \"\"\"Парсер hh.ru API (real impl).\"\"\" 
    url = f\"https://api.hh.ru/vacancies?text={query}&area={area}&per_page=10\"
    
    try:
        response = requests.get(url, headers={\"User-Agent\": \"JobAgent/1.0\"})
        data = response.json()
        
        vacancies = []
        for item in data[\"items\"]:
            vacancies.append({
                \"id\": item[\"id\"],
                \"name\": item[\"name\"],
                \"employer\": item[\"employer\"][\"name\"],
                \"salary\": item.get(\"salary\", {}),
                \"url\": item[\"alternate_url\"],
                \"description\": item[\"snippet\"][\"requirement\"]
            })
        return vacancies
    except Exception as e:
        return [{\"error\": str(e)}]

# Stub для LangChain tool
def job_search_tool(query: str) -> str:
    result = asyncio.run(search_hh_ru(query))
    return str(result)

if __name__ == \"__main__\": 
    import asyncio
    print(asyncio.run(search_hh_ru(\"Python developer\")))

