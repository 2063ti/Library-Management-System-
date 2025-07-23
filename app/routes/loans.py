# from fastapi import APIRouter, Depends, HTTPException
# from tortoise.contrib.fastapi import HTTPNotFoundError
# from app import models, schemas

# router = APIRouter(
#     prefix="/loans",
#     tags=["loans"]
# )

# @router.post("/", response_model=schemas.LoanRead)
# async def create_loan(loan: schemas.LoanCreate):
#     obj = await models.Loan.create(**loan.dict())
#     return await schemas.LoanRead.from_tortoise_orm(obj)
