
import os
import requests

def test_gpt():
    key = os.getenv("YANDEX_API_KEY")
    folder_id = os.getenv("YANDEX_FOLDER_ID")

    if not key or not folder_id:
        print("? е заданы переменные окружени€")
        return

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {"Authorization": f"Api-Key {key}"}
    data = {
        "modelUri": f"gpt://{folder_id}/yandexgpt/latest",
        "messages": [{"role": "user", "text": "бъ€сни, что такое системное мышление"}],
        "temperature": 0.5,
        "maxTokens": 500
    }

    try:
        resp = requests.post(url, headers=headers, json=data)
        print("? твет:", resp.json()["result"]["alternatives"][0]["message"]["text"])
    except Exception as e:
        print(f"? шибка: {e}")

if __name__ == "__main__":
    test_gpt()

