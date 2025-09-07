from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


app = FastAPI()

# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


todos = []

class Todo(BaseModel):
    id:int
    name:str
    completed:bool = False

@app.get("/")
def read_root():
    return {"message": "Welcome to ToDo API"}

@app.get("/todos" ,   response_model=List[Todo])
def return_todos():
    return todos

@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")



@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Deleted successfully"}









