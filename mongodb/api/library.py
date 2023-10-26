from config.settings import app
from ..schemas.book_models import Book
        

@app.get("/")
def get_all_books():
    return Book.all()


@app.get("/{item_id}")
def read_item(item_id: str):
    return Book.get({"_id": item_id}) 


@app.post("/create")
def create_book(book: Book):
    return {'_id': book.save()}
    

@app.put("/{item_id}/update")
def update_book(item_id: str, book: Book):
    return book.save(item_id)
     

@app.post("/delete/{item_id}")
def delete_book(item_id: str):
    Book.delete(item_id)
    return {'message': 'item deleted'}