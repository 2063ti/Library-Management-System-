
# from FastAPI import FastAPI, Depends,Session
# from  app.database import get_db
# from fastapi import HTTPException

# @app.post("/books/", response_model=schemas.BookRead)
# def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
#     db_book = models.Book(
#         title=book.title,
#         isbn=book.isbn,
#         publication_year=book.publication_year,
#         publisher=book.publisher,
#         copies_available=book.copies_available
#     )
#     db_book.authors = db.query(models.Author).filter(models.Author.id.in_(book.author_ids)).all()
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book

# from fastapi import FastAPI
# from app.routes import authors, books, members, staff, loans

# app = FastAPI()

# app.include_router(authors.router)
# app.include_router(books.router)
# app.include_router(members.router)
# app.include_router(staff.router)
# app.include_router(loans.router)


from fastapi import FastAPI
from app.config import init_db
from app.routes import author
from app.routes import book
from app.routes import members
from app.routes import staff
from app.routes import loans

app = FastAPI(title="Library Management System")



@app.on_event("startup")
async def startup_event():
    print("Starting up the Library Management System...")
    await init_db()


app.include_router(author.router, prefix="/author", tags=["author"])
app.include_router(book.router, prefix="/book", tags=["book"])
app.include_router(members.router, prefix="/member", tags=["member"])
app.include_router(staff.router, prefix="/staff", tags=["staff"])
app.include_router(loans.router, prefix="/loan", tags=["loan"])