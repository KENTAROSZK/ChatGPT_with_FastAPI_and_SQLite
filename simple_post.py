import requests
import json


url = "http://localhost:8000/process/"  # POSTリクエストを送信するエンドポイントのURL

data = {
    "user_id": "example_user",
    "query"  : "example_query"
}

response = requests.post(url, json=data)

# レスポンスの内容を表示
print(response.json())