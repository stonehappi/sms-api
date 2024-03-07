
from pydantic import BaseModel


class InsertNewCompanyName(BaseModel):
    name: str
    address: str

class UpdateCompany(BaseModel):
    name: str
    address: str