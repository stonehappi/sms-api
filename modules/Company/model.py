from pydantic import BaseModel 

class CompanyListResponse(BaseModel):
    name: str
    address: str
class CompanyInsertRequest(BaseModel):  # type: ignore
    name: str
    address: str
class ComapanyUpdateRequest(BaseModel):  # type: ignore
    name: str
    address: str