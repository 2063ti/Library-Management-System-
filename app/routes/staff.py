from fastapi import APIRouter
from app.schemas import StaffCreate, StaffUpdate, StaffLoginSchema,StaffRead
from app.crud import staff as staff_crud

router = APIRouter()


@router.post("/", response_model=StaffRead)
async def register_staff(data: StaffCreate):
    return await staff_crud.create_staff(data)

@router.post("/login")
async def login_staff(data: StaffLoginSchema):
    return await staff_crud.login_staff(data)