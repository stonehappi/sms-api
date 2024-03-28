from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db, SessionLocal
from modules.Position.model import PositionInsertRequest, PositionUpdateRequest
from modules.Position.entity import Position

router = APIRouter(prefix="/Position", tags=["Position"])


@router.get("/read/")
def get(db: Session = Depends(get_db)):
    Positions = db.query(Position).all()
    return Positions


@router.post("/create/")
def create(request:  PositionInsertRequest, db: Session = Depends(get_db)):
    item = Position(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/update/{item_id}")
def update(item_id: int, request: PositionUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Position).filter(Position.id == item_id).first()
    if old_item:
        old_item.name = request.name
        old_item.companyid = request.companyid
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "shit your Item not found"}

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Position).filter(Position.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item already deleted successfully"}
    return {"message": "Item cannot found"}
