from pydantic import BaseModel

class StudentListResponse(BaseModel):
    id: int
    name: str
    address: str
    age: int

class StudentInsertRequest(BaseModel):
    name: str
    address: str
    age: int

class StudentUpdateRequest(BaseModel):
    name: str
    address: str
    age: int

