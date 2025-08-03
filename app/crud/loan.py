from app.models.models import Loan, Book, Member, Staff
from app.schemas import LoanCreate, LoanReturnSchema
from tortoise.exceptions import DoesNotExist
from fastapi import HTTPException
from datetime import date

async def create_loan(data:LoanCreate):
    try:
        book = await Book.get(id=data.book_id)
        member = await Member.get(id=data.member_id)
        staff = await Staff.get(id=data.staff_id)

        loan = await Loan.create(
            book=book,
            member=member,
            staff=staff,
            due_date=data.due_date
            # due_date=data.due_date.isoformat() if isinstance(data.loan_date, date) else data.loan_date,
        )

        return loan
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Book, Member, or Staff not found")
    

async def get_all_loans():
    return await Loan.all().prefetch_related("book", "member", "staff")

async def get_loan_by_id(loan_id: int):
    loan = await Loan.get_or_none(id=loan_id).prefetch_related("book", "member", "staff")
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan

async def return_loan(loan_id: int, data: LoanReturnSchema):
    loan = await Loan.get_or_none(id=loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    if loan.returned:
        raise HTTPException(status_code=400, detail="Loan already returned")
    
    loan.return_date = data.return_date
    loan.returned = True
    await loan.save()
    return loan

async def delete_loan(loan_id: int):
    loan = await Loan.get_or_none(id=loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    await loan.delete()
    return {"message": "Loan deleted successfully"}
