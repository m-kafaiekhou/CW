from schemas.book_models import Book
from fastapi import APIRouter

router = APIRouter()
        

@router.get("/")
def get_all_books():
    return Book.all()


@router.get("/{item_id}")
def read_item(item_id: str):
    return Book.get({"_id": item_id}) 


@router.post("/create")
def create_book(book: Book):
    return {'_id': book.save()}
    

@router.put("/{item_id}/update")
def update_book(item_id: str, book: Book):
    return book.save(item_id)
     

@router.post("/delete/{item_id}")
def delete_book(item_id: str):
    Book.delete(item_id)
    return {'message': 'item deleted'}