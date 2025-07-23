from app.models.models import Book,Author
from app.schemas import BookCreate,AuthorRead,BookRead
from typing import List,Optional
from tortoise.exceptions import DoesNotExist


# async def create_book(book_data: BookCreate)->Book:
#     # Create the book itself (excluding authors)
#     book = await Book.create(
#         title=book_data.title,
#         isbn=book_data.isbn,
#         publication_year=book_data.publication_year,
#         publisher=book_data.publisher,
#         copies_available=book_data.copies_available
#     )
     
#     # Link authors
#     if book_data.author_ids:
#         authors = await Author.filter(id__in=book_data.author_ids)
#         await book.authors.add(*authors)
    
#     return book
from fastapi import HTTPException

async def create_book(book_data: BookCreate) -> Book:
    # Check for duplicate ISBN
    if book_data.isbn:
        existing_book = await Book.get_or_none(isbn=book_data.isbn)
        if existing_book:
            raise HTTPException(status_code=400, detail="ISBN already exists.")

    # Create the book
    book = await Book.create(
        title=book_data.title,
        isbn=book_data.isbn,
        publication_year=book_data.publication_year,
        publisher=book_data.publisher,
        copies_available=book_data.copies_available
    )

    # Link authors
    if book_data.author_ids:
        authors = await Author.filter(id__in=book_data.author_ids)
        await book.authors.add(*authors)

    # Fetch with authors preloaded
    return await Book.get(id=book.id).prefetch_related('authors')


async def get_all_books() -> List[Book]:
    return await Book.all().prefetch_related("authors")


async def get_book_by_id(book_id: int) -> Optional[Book]:
    return await Book.get_or_none(id=book_id).prefetch_related("authors")


async def update_book(book_id: int, book_data: BookCreate) -> Optional[Book]:
    book = await Book.get_or_none(id=book_id)
    if not book:
        return None
    
    # Update basic fields
    book.title = book_data.title
    book.isbn = book_data.isbn
    book.publication_year = book_data.publication_year
    book.publisher = book_data.publisher
    book.copies_available = book_data.copies_available
    await book.save()

    # Update authors
    if book_data.author_ids is not None:
        authors = await Author.filter(id__in=book_data.author_ids)
        await book.authors.clear()
        await book.authors.add(*authors)

    author_data = await book.authors.all().values("id", "name")  # Add fields if needed
    authors_list = [AuthorRead(**author) for author in author_data]
    
    # return book
    return BookRead(
        id=book.id,
        title=book.title,
        isbn=book.isbn,
        publication_year=book.publication_year,
        publisher=book.publisher,
        copies_available=book.copies_available,
        authors=authors_list
    )


async def delete_book(book_id: int) -> int:
    return await Book.filter(id=book_id).delete()