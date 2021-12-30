from fastapi import FastAPI

from models import User

app = FastAPI()


@app.post("/start/{user_id}")
async def start(user_id):
    User.insert(user_id)
    data = {"message": "Добро пожаловать!", "user_id": user_id}
    return data
