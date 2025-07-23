from typing import List, Optional

from app.models.models import Author
from app.schemas import AuthorCreate

from tortoise.exceptions import DoesNotExist

async def create_author(author_data: AuthorCreate) -> Author:
    author = await Author.create(**author_data.dict())
    return author

async def get_all_authors() -> List[Author]:
    return await Author.all()

async def get_author_by_id(author_id: int) -> Optional[Author]:
    return await Author.get_or_none(id=author_id)

async def update_author(author_id: int, author_data: AuthorCreate) -> Optional[Author]:
    author = await Author.get_or_none(id=author_id)
    if not author:
        return None
    author.name = author_data.name
    author.bio = author_data.bio
    await author.save()
    return author

async def delete_author(author_id: int) -> int:
    deleted_count = await Author.filter(id=author_id).delete()
    return deleted_count
