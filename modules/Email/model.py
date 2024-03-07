from pydantic import BaseModel

class EmailListResponse(BaseModel):
    id: int
    mail: int
    name: str
    Contact_id: int

class EmailInsertRequest(BaseModel):
    mail: int
    name: str
    Contact_id: int

class EmailUpdateRequest(BaseModel):
    mail: int
    name: str
    Contact_id: int

class EmailDeleteRequest(BaseModel):
    mail: int
    name: str
    Contact_id: int
