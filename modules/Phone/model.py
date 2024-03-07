from pydantic import BaseModel

class PhoneListResponse(BaseModel):
    id: int
    number: int
    name: str
    Contact_id: int

class PhoneInsertRequest(BaseModel):
    number: int
    name: str
    Contact_id: int

class PhoneUpdateRequest(BaseModel):
    number: int
    name: str
    Contact_id: int

class PhoneDeleteRequest(BaseModel):
    number: int
    name: str
    Contact_id: int
