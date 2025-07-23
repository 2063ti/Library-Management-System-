from app.models import Member
from app.schemas import MemberCreate, MemberUpdate
from app.utils.security import hash_password
from fastapi import HTTPException

async def create_member(data:MemberCreate):
    existing = await Member.get_or_none(email=data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Member with this email already exists.")
    hashed_password = hash_password(data.password)
    member = await Member.create(
        name=data.name,
        email=data.email,
        phone=data.phone,
        address=data.address,
        password=hashed_password
    )

    return member

async def get_all_members():
    return await Member.all()

async def get_member_by_id(member_id: int):
    member = await Member.get_or_none(id=member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found.")
    return member

async def update_member(member_id: int, data: MemberUpdate):
    member = await Member.get_or_none(id=member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found.")
    
    update_data = data.model_dump(exclude_unset=True)

    if "password" in update_data:
        update_data["password"] = hash_password(update_data.pop("password"))
    
    await member.update_from_dict(update_data).save()
    return member

async def delete_member(member_id: int):
    member = await Member.get_or_none(id=member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    await member.delete()
    return {"message": "Member deleted successfully"}