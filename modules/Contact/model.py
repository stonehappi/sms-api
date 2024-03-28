from pydantic import BaseModel 

class ContactListResponse(BaseModel):
    Id: int
    Firstname: str
    Lastname: str
    Positionid: int
class ContactInsertRequest(BaseModel):  # type: ignore
    Firstname: str
    Lastname: str
    Positionid: int
class ContactUpdateRequest(BaseModel):  # type: ignore
    Firstname: str
    Lastname: str
    Positionid: int