from enum import Enum

class StaffRole(str, Enum):
    ADMIN = "admin"
    LIBRARIAN = "librarian"
    ASSISTANT = "assistant"