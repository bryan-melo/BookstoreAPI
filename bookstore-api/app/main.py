from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the Bookstore API!!"}


@app.get('/todos/{to_do}')
async def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return { "todo":todo }