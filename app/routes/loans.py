from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import LoanCreate, LoanReturnSchema, LoanOut
from app.crud import loan as loan_crud

router = APIRouter()

@router.post("/",response_model=LoanOut)
async def create_loan(data:LoanCreate):
    return await loan_crud.create_loan(data)


@router.get("/",response_model=List[LoanOut])
async def get_all_loans():
    return await loan_crud.get_all_loans()


@router.get("/{loan_id}", response_model=LoanOut)
async def get_loan(loan_id: int):
    return await loan_crud.get_loan_by_id(loan_id)


@router.put("/{loan_id}/return", response_model=LoanOut)
async def return_loan(loan_id: int, data: LoanReturnSchema):
    return await loan_crud.return_loan(loan_id, data)


@router.delete("/{loan_id}")
async def delete_loan(loan_id: int):
    return await loan_crud.delete_loan(loan_id)
