from pydantic import BaseModel


class PositionListResponse(BaseModel):
    id: int
    name: str
    company_id: int


class PositionInsertRequest(BaseModel):
    name: str
    company_id: int


class PositionUpdateRequest(BaseModel):
    name: str
    company_id: int
