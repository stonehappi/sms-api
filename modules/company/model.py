from pydantic import BaseModel


class companyInsertRequest(BaseModel):
    name : str
    address : int
class companyUpdateRequest(BaseModel):
    name : str
    address : int
