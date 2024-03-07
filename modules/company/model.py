from pydantic import BaseModel


class companyInsertRequest(BaseModel):
    Name : str
    Address : int
class companyUpdateRequest(BaseModel):
    Name : str
    Address : int
