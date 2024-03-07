from pydantic import BaseModel

class ContactListResponse(BaseModel):
    id: int
    First_name: str
    Last_name: str
    Position_id: int

class ContactInsertRequest(BaseModel):
    First_name: str
    Last_name: str 
    Position_id: int

class ContactUpdateRequest(BaseModel):
    First_name: str
    Last_name: str
    Position_id: int

class ContactDeleteRequest(BaseModel):
    First_name: str
    Last_name: str
    Position_id: int

