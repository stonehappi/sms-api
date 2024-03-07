from pydantic import BaseModel

class CompanyListResponse(BaseModel):
    id: int
    name: str
    Address: str 

class CompanyInsertRequest(BaseModel):
    name: str
    Address: str 

class CompanyUpdateRequest(BaseModel):
    name: str
    Address: str 

class CompanyDeleteRequest(BaseModel):
    name: str
    Address: str 


