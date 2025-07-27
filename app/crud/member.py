from app.models.models import Member
from app.schemas import MemberCreate, MemberUpdate,MemberLoginSchema
from app.utils.security_auth import hash_password,verify_password
from fastapi import HTTPException,status
from pydantic import EmailStr, Field
async def create_member(data:MemberCreate):
    existing = await Member.get_or_none(email=data.email)
    print("got it1")
    if existing:
        print("got it2")
        raise HTTPException(status_code=400, detail="Member with this email already exists.")
    hashed_password = hash_password(data.password)
    print("got it  paas",hashed_password)
    member = await Member.create(
        name=data.name,
        email=data.email,
        phone=data.phone,
        address=data.address,
        password_hash=hashed_password
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

async def login_member(data:MemberLoginSchema):
    member = await Member.get_or_none(email=data.email)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not verify_password(data.password, member.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    return {
        "message": "Login successful",
        "member_id": member.id,
        "email": member.email,
        "name": member.name
        # You can also return token here (e.g. JWT) if using authentication
    }