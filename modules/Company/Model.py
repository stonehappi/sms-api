from pydantic import BaseModel


class CompanyInsertRequest(BaseModel):
    name: str
    address : str
class CompanyUpdateRequest(BaseModel):
    name : str
    address : str
class CompanyRespon(BaseModel):
    name : str
    address : str
