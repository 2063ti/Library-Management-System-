from typing import List, Optional
from datetime import date
from pydantic import BaseModel,EmailStr, Field
from datetime import datetime
from app.enums import StaffRole
# --- Author ---
class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class AuthorRead(AuthorBase):
    id: int
    class Config:
        from_attributes = True
# --- Book ---
class BookBase(BaseModel):
    title: str
    isbn: Optional[str] = None
    publication_year: Optional[int] = None
    publisher: Optional[str] = None
    copies_available: Optional[int] = 0

class BookCreate(BookBase):
    author_ids: List[int]  # For assigning authors during creation

class BookRead(BookBase):
    id: int
    authors: List[AuthorRead] = []
    class Config:
        from_attributes = True

# --- Member ---
class MemberCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    password: str  # Raw password

class MemberOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None
    membership_date: datetime

    class Config:
        from_attributes = True

class MemberLoginSchema(BaseModel):
    email: EmailStr
    password: str 


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None  # Optional password update


# --- Staff ---
class StaffBase(BaseModel):
    name: str
    email: str
    role: Optional[StaffRole]

class StaffCreate(StaffBase):
    pass

class StaffRead(StaffBase):
    id: int
    class Config:
        from_attributes = True

# --- Loan ---
class LoanBase(BaseModel):
    book_id: int
    member_id: int
    staff_id: int
    loan_date: date
    due_date: date
    return_date: Optional[date] = None
    returned: bool = False

class LoanCreate(LoanBase):
    pass

class LoanRead(LoanBase):
    id: int
    class Config:
        from_attributes = True
