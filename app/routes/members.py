from fastapi import APIRouter
from typing import List
from app.schemas import MemberCreate,MemberOut,MemberUpdate,MemberLoginSchema
from app.crud import member as member_crud

router = APIRouter()

@router.post("/", response_model=MemberOut)
async def create_member(data: MemberCreate):
    print("Creating member with data:", data)
    return await member_crud.create_member(data)


@router.post("/login/")
async def login_member(data: MemberLoginSchema):
    print("Logging in member with data:", data)
    return await member_crud.login_member(data)

@router.get("/",response_model=List[MemberOut])
async def get_members():
    return await member_crud.get_all_members()

@router.get("/{member_id}",response_model=MemberOut)
async def get_member(member_id: int):
    return await member_crud.get_member_by_id(member_id)

@router.put("/{member_id}",response_model=MemberOut)
async def update_member(member_id:int,data:MemberUpdate):
    return await member_crud.update_member(member_id, data)

@router.delete("/{member_id}", response_model=MemberOut)
async def delete_member(member_id: int):
    return await member_crud.delete_member(member_id)