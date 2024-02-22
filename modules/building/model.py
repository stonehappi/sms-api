from datetime import datetime
from pydantic import BaseModel


class BuildingListResponse(BaseModel):
    id: int
    name: str
    floor: int
    roos: int
    # date: datetime
    draft: bool


class BuildingInsertRequest(BaseModel):
    name: str
    floor: int
    roos: int
    date: datetime
    draft: bool


class BuildingUpdateRequest(BaseModel):
    floor: int
    roos: int
    date: datetime
    draft: bool
