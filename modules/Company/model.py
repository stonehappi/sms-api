from pydantic import BaseModel

class CompanyListResponse(BaseModel):
    id: int
    Owner: str
    Founded: int 
    Staff: int 
    department: int 
    location: str 
    email: str 


class CompanyInsertRequest(BaseModel):
    Owner: str
    Founded: int 
    Staff: int 
    department: int 
    location: str 
    email: str 

class CompanyUpdateRequest(BaseModel):
    Owner: str
    Founded: int 
    Staff: int 
    department: int 
    location: str 
    email: str 

class CompanyDeleteRequest(BaseModel):
    Owner: str
    Founded: int 
    Staff: int 
    department: int 
    location: str 
    email: str 