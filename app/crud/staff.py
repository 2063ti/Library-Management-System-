from app.models.models import Staff
from app.schemas import StaffCreate,  StaffLoginSchema
from app.utils.security_auth import hash_password,verify_password
from fastapi import HTTPException, status

async def create_staff(data:StaffCreate):
    existing = await Staff.get_or_none(email=data.email)
    if existing :
        raise HTTPException(status_code=400, detail="Staff with this email already exists.")
    
    staff = await Staff.create(
        name = data.name,
        email = data.email,
        phone = data.phone,
        address = data.address,
        role = data.role,
        password_hash = hash_password(data.password)
    )

    return staff

async def get_all_staff():
    return await Staff.all()

async def login_staff(data: StaffLoginSchema):
    staff = await Staff.get_or_none(email=data.email)
    if not staff or not verify_password(data.password, staff.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return {
        "message": "Login successful",
        "staff_id": staff.id,
        "email": staff.email,
        "name": staff.name
    }


async def get_staff_by_id(staff_id: int):
    staff = await Staff.get_or_none(id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

async def delete_staff(staff_id: int):
    staff = Staff.get_or_none(id=staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    
    await staff.delete()

    return {"message": "Staff deleted successfully"}
