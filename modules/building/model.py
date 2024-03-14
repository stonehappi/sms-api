from pydantic import BaseModel


class BuildingListResponse(BaseModel):
    id: int
    name: str


class BuildingInsertRequest(BaseModel):
    name: str


class BuildingUpdateRequest(BaseModel):
    name: str
