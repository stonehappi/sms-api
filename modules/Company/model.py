from pydantic import BaseModel

class CompanyListResponse(BaseModel):
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