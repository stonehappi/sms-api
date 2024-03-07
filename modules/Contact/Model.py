from pydantic import BaseModel


class ContactInsertRequest(BaseModel):
    FirstName : str
    LastName : str
    PositionId : int

class ContactUpdateRequest(BaseModel):
    FirstName : str
    LastName : str
    PositionId : int
class ContactRespon(BaseModel):
    FirstName : str
    LastName : str
    PositionId : int
