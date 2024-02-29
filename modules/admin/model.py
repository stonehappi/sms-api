
from pydantic import BaseModel


class AdminInsertRequest(BaseModel):
    fullname:str
    password:str
    device:int

class AdminUpdateRequest(BaseModel):
    fullname:str
    password:str
    device:int 
