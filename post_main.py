import requests
import json
import os
import sqlite3
import pandas as pd


url = "http://localhost:8000/process/"  # POSTリクエストを送信するエンドポイントのURL

data = {
    "user_id": "example_user",
    "query"  : "最初に学ぶプログラミング言語でおすすめを理由と合わせて3つ教えてください"
}

response = requests.post(url, json=data)

# レスポンスの内容を表示
#print(response.json())

# ステータスコードを取得
status_code = response.status_code
print("status : " + str(status_code))


# データベースファイルのパス
DB_PATH = 'chat_history.db'

# データベースに接続
conn   = sqlite3.connect(DB_PATH)

# SQLクエリを実行し、データを取得
query = "SELECT * FROM data"
df    = pd.read_sql_query(query, conn)




# データベース接続を閉じる
conn.close()



# データフレームを表示
print(df)



# chatGPTの回答を一覧で確認する
for _ in range(3):
	print()

for output in df["OUTPUT"].values.tolist():
	print(output)