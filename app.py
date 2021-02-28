from typing import Optional
from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel

# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date


app = FastAPI()


@app.get("/")
def get_status():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/users")
def get_user(user: User):
    return user.name
