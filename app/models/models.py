from tortoise import fields, models
from app.enums import StaffRole

class Author(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    bio = fields.TextField(null=True)

    books: fields.ManyToManyRelation["Book"]
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    isbn = fields.CharField(max_length=13, unique=True,null=True)
    publication_year = fields.IntField(null=True)
    publisher = fields.CharField(max_length=255, null=True)
    copies_available = fields.IntField(default=0)
    
    authors = fields.ManyToManyField("models.Author", related_name="books")
    loans: fields.ReverseRelation["Loan"]

    def __str__(self):
        return self.title
    
class Member(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    phone = fields.CharField(max_length=20, null=True)
    address = fields.TextField(null=True)
    password_hash = fields.CharField(max_length=255)  # Store hashed passwords
    membership_date = fields.DatetimeField(auto_now_add=True)


    loans: fields.ReverseRelation["Loan"]

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)
    password_hash= fields.CharField(max_length=255)  # Store hashed passwords
    role = fields.CharField(max_length=50, default=StaffRole.LIBRARIAN.value)
    phone = fields.CharField(max_length=20, null=True)
    address = fields.TextField(null=True)
    joined_on = fields.DatetimeField(auto_now_add=True)

    loans: fields.ReverseRelation["Loan"]

    def __str__(self):
        return f"{self.name} ({self.role})"
    
class Loan(models.Model):
    id = fields.IntField(pk=True)
    book = fields.ForeignKeyField("models.Book", related_name="loans", on_delete=fields.CASCADE)
    member = fields.ForeignKeyField("models.Member", related_name="loans", on_delete=fields.CASCADE)
    staff = fields.ForeignKeyField("models.Staff", related_name="loans", on_delete=fields.CASCADE, null=True)
    loan_date = fields.DatetimeField(auto_now_add=True)
    return_date = fields.DatetimeField(null=True)
    due_date = fields.DatetimeField()
    returned = fields.BooleanField(default=False) 


    def __str__(self):
        return f"Loan of {self.book.title} to {self.member.name}"
    
