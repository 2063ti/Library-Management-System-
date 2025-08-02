from fastapi import APIRouter
from typing import List
from app.schemas import StaffCreate, StaffLoginSchema,StaffRead,StaffOutSchema
from app.crud import staff as staff_crud

router = APIRouter()


@router.post("/", response_model=StaffRead)
async def register_staff(data: StaffCreate):
    return await staff_crud.create_staff(data)

@router.post("/login")
async def login_staff(data: StaffLoginSchema):
    return await staff_crud.login_staff(data)

@router.get("/", response_model=List[StaffOutSchema])
async def get_all_staff():
    return await staff_crud.get_all_staff()

@router.delete("/{staff_id}", response_model=dict)
async def delete_staff(staff_id: int):
    print("Deleting staff with ID:", staff_id)
    return await staff_crud.delete_staff(staff_id)


@router.get("/{staff_id}",response_model=StaffOutSchema)
async def get_staff(staff_id: int):
    return await staff_crud.get_staff_by_id(staff_id)