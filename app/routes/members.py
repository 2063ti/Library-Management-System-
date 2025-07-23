# from fastapi import APIRouter, HTTPException
# from app.models import models
# from app import schemas
# from app.utils import auth
# from typing import List

# router = APIRouter(
#     prefix="/members",
#     tags=["members"]
# )

# # Create/Register a new member
# @router.post("/", response_model=schemas.MemberRead)
# async def register_member(member: schemas.MemberCreate):
#     hashed = auth.hash_password(member.password)
#     obj = await models.Member.create(
#         name=member.name,
#         email=member.email,
#         password_hash=hashed,
#         phone=member.phone,
#         address=member.address,
#         membership_date=member.membership_date
#     )
#     return await schemas.MemberRead.from_tortoise_orm(obj)

# # List all members
# @router.get("/", response_model=List[schemas.MemberRead])
# async def list_members():
#     return await schemas.MemberRead.from_queryset(models.Member.all())

# # Get single member
# @router.get("/{id}", response_model=schemas.MemberRead, responses={404: {"model": HTTPException}})
# async def get_member(id: int):
#     return await schemas.MemberRead.from_queryset_single(models.Member.get(id=id))

# # Update member
# @router.put("/{id}", response_model=schemas.MemberRead)
# async def update_member(id: int, member: schemas.MemberBase):
#     await models.Member.filter(id=id).update(**member.dict())
#     return await schemas.MemberRead.from_queryset_single(models.Member.get(id=id))

# # Delete member
# @router.delete("/{id}")
# async def delete_member(id: int):
#     deleted_count = await models.Member.filter(id=id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail="Member not found")
#     return {"deleted": True}
