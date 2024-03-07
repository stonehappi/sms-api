from pydantic import BaseModel


class positionInsertRequest(BaseModel):
    name  : str
    Address : int
class positionUpdateRequest(BaseModel):
    name  : str
    CompanyId : int
