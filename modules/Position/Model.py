from pydantic import BaseModel


class PositionInsertRequest(BaseModel):
    Name : str
    CompanyId : int

class PositionUpdateRequest(BaseModel):
    Name : str
    CompanyId : int
class PositionRespon(BaseModel):
    Name : str
    CompanyId : int
