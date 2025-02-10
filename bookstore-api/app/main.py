from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the Bookstore API!!"}


# Updata a todo
@app.get('/todos/{to_do}')
async def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return { "todo":todo }
        

# Delete a todo
@app.delete("/todos/{to_do}")
async def delete_todo(todo_int: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            

# Get book by book id
@app.get_book('/get-book/{book_id}')
async def get_book(book_id: int):
    if book_id in books:
        return { "book": books[book_id] }
    else:
        return  { "error": "book not in library." }
        

# Delete book by book id
@app.delete("/delete-book/{book_id}")
async def delete_book(book_id: int):
    if book_id in books:
        books.delete(books[book_id])
        return { "deleted": "book deleted"}
    else:
        return { "error": "The book you are trying to remove does not exist in this library. "}
        