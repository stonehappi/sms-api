from pydantic import BaseModel 

class PositonListResponse(BaseModel):
    id: int
    name: str
    companyid: int
class PositionInsertRequest(BaseModel):  # type: ignore
    name: str
    companyid: int
class PositionUpdateRequest(BaseModel):  # type: ignore
    name: str
    companyid: int