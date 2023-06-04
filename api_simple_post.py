from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    user_id: str
    query: str

class Output(BaseModel):
    user_id: str
    query: str
    output: str

@app.post("/process/")
def main(input_data: Input):
    # 入力データを取得
    user_id = input_data.user_id
    query = input_data.query

    # 文字列の加工処理
    processed_text = f"Processed _ User ID: {user_id}, Query: {query}"

    # 処理結果と入力データをまとめて返す
    output_data = Output(user_id=user_id, query=query, output=processed_text)
    return output_data
