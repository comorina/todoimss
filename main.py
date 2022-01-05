from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


origins = [
    "https://comorina.github.io/FastApiExample/",
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        
)
todos = []
users = []

class Course(BaseModel):
    todo : str

class UserData(BaseModel):

    username : str


@app.get("/user", tags=['users'])
async def root()->dict:
    return {"data" : users}   

@app.post("/user", tags=["users"])
def add_User(user:UserData) -> dict:
    users.append(user.dict())
    return users[-1]


@app.get("/todo", tags=['todos'])
async def root()->dict:
    return {"data" : todos}


@app.post("/todo", tags=["todos"])
def add_todo(todo:Course) -> dict:
    todos.append(todo.dict())
    return todos[-1]
    
@app.delete("/todo/delete", tags=["todos"])
async def delete_Todo(id:int) ->dict:
    for todo in todos:
        if( todo["id"] == id ):
            todos.remove(todo)
    return todos