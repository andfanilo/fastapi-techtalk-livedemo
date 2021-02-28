# FastAPI Live Demo

## Prerequisites

```
conda create -n fastapi python=3.7
conda activate fastapi
pip install fastapi pytest
```

## Run

```
uvicorn app:app --reload
```

## Demo steps

### Part 1 - First steps 

- Create empty `app.py`
- Open terminal with `CTRL + SHIFT + ù`. Run `uvicorn app:app --reload`
- Open `http://localhost:8000` and `http://localhost:8000/docs`
- Enter some code in `app.py`: 

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_status():
    return {"Hello": "World"}
```
- Check browser and docs. Change name of function and see interactive docs change.

### Part 2 - Static type hints

- Add some code 

```python
@app.get("/items/{item_id}")
def read_item(item_id, q = None):
    return {"item_id": item_id, "q": q}
```
    - see now `item_id` is required

- Use static hints

```python
from typing import Optional 
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```
    - see in docs that typings have changed

- Use modern Python type declarations with Pydantic

```python
from typing import List, Dict
from datetime import date

from pydantic import BaseModel

# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date

@app.post("/users")
def get_user(user: User):
    return user.name
```
- showoff type inference/autocompletion on `user.name` in editor

- Reformat code with Black: `black app.py`

### Part 3 - Unit testing

```python
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_status():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_post_user():
    response = client.post("/users", json={
        "id": 4,
        "name": "Mary",
        "joined": "2018-11-30",
    })
    assert response.status_code == 200
    assert response.json() == "Mary"
```

- Run with `pytest test_app.py`