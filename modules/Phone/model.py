from pydantic import BaseModel


class phoneInsertRequest(BaseModel):
    number:str
    name:str
    contactid:int


class phoneUpdateRequest(BaseModel):
    number:str
    name:str
    contactid:int
