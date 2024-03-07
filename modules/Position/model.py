from pydantic import BaseModel

class PositionListResponse(BaseModel):
    id: int
    name: str
    Company_id: int

class PositionInsertRequest(BaseModel):
    name: str
    Company_id: int
class PositionUpdateRequest(BaseModel):
    name: str
    Company_id: int

class PositionDeleteRequest(BaseModel):
    name: str
    Company_id: int

