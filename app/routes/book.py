from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import BookCreate, BookRead
from app.crud import book as book_crud

router = APIRouter()

@router.post("/", response_model=BookRead)
async def create_book(book: BookCreate):
    return await book_crud.create_book(book)

@router.get("/", response_model=List[BookRead])
async def list_books():
    return await book_crud.get_all_books()

@router.get("/{book_id}", response_model=BookRead)
async def get_book(book_id: int):
    result = await book_crud.get_book_by_id(book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return result

@router.put("/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book: BookCreate):
    result = await book_crud.update_book(book_id, book)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return result

@router.delete("/{book_id}")
async def delete_book(book_id: int):
    deleted = await book_crud.delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"deleted": deleted}
