# from fastapi import APIRouter, Depends, HTTPException
# from tortoise.contrib.fastapi import HTTPNotFoundError
# from app import models, schemas
# from typing import List

# router = APIRouter(
#     prefix="/authors",
#     tags=["authors"]
# )

# @router.post("/", response_model=schemas.AuthorRead)
# async def create_author(author: schemas.AuthorCreate):
#     obj = await models.Author.create(**author.dict())
#     return await schemas.AuthorRead.from_tortoise_orm(obj)

# @router.get("/", response_model=List[schemas.AuthorRead])
# async def list_authors():
#     return await schemas.AuthorRead.from_queryset(models.Author.all())

# @router.get("/{id}", response_model=schemas.AuthorRead, responses={404: {"model": HTTPNotFoundError}})
# async def get_author(id: int):
#     return await schemas.AuthorRead.from_queryset_single(models.Author.get(id=id))

# @router.put("/{id}", response_model=schemas.AuthorRead)
# async def update_author(id: int, author: schemas.AuthorCreate):
#     await models.Author.filter(id=id).update(**author.dict())
#     return await schemas.AuthorRead.from_queryset_single(models.Author.get(id=id))

# @router.delete("/{id}")
# async def delete_author(id: int):
#     deleted_count = await models.Author.filter(id=id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail="Author not found")
#     return {"deleted": True}


from fastapi import APIRouter, HTTPException
from app.schemas import AuthorCreate, AuthorRead
from app.crud import author as author_crud
from typing import List
router = APIRouter()

@router.post("/", response_model=AuthorRead)
async def create_author(author: AuthorCreate):
    return await author_crud.create_author(author)

@router.get("/", response_model=List[AuthorRead])
async def list_authors():
    return await author_crud.get_all_authors()

@router.get("/{author_id}", response_model=AuthorRead)
async def get_author(author_id: int):
    result = await author_crud.get_author_by_id(author_id)
    if not result:
        raise HTTPException(status_code=404, detail="Author not found")
    return result

@router.put("/{author_id}", response_model=AuthorRead)
async def update_author(author_id: int, author: AuthorCreate):
    result = await author_crud.update_author(author_id, author)
    if not result:
        raise HTTPException(status_code=404, detail="Author not found")
    return result

@router.delete("/{author_id}")
async def delete_author(author_id: int):
    deleted = await author_crud.delete_author(author_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Author not found")
    return {"deleted": deleted}
