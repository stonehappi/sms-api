

from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.position.entity import Position





router = APIRouter(prefix="/position", tags=["positon"])
@router.get("Create")
def read(db: SessionLocal = Depends(get_db)):
    return db.query(Position).all()

@router.get("Read")
def create():
    return"create position"


@router.get("Update")
def update():
    return"update position"


@router.get("Delete")
def delete():
    return"delete position"