from pydantic import BaseModel


class positionInsertRequest(BaseModel):
    name  : str
    CompanyId : int
class positionUpdateRequest(BaseModel):
    name  : str
    CompanyId : int
