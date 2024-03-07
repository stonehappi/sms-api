from pydantic import BaseModel


class emailInsertRequest(BaseModel):
    Mail:str
    Name:str
    Contactid: int
class emailUpdateRequest(BaseModel):
    Mail:str
    Name:str
    Contactid: int
