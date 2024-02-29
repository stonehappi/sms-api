from pydantic import BaseModel


class PositionListResponse(BaseModel):
    id: int
    name: str


class PositionInsertRequest(BaseModel):
    positonname: str
    salary: int
    Address : str
    email : str
    Sex : str
    Fullname : str

class PositionUpdateRequest(BaseModel):
    name: str
    Salary: int
    CurrentAddress : str
    email : str
    responsibility : str
    newposition : str
    datetime : int 

    


