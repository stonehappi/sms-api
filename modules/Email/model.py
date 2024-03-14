from pydantic import BaseModel

class EmailListResponse(BaseModel):
    id: int
    mail: str
    name: str
    Contact_id: int

class EmailInsertRequest(BaseModel):
    mail: str
    name: str
    Contact_id: int

class EmailUpdateRequest(BaseModel):
    mail: str
    name: str
    Contact_id: int

class EmailDeleteRequest(BaseModel):
    mail: str
    name: str
    Contact_id: int
