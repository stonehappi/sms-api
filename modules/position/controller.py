from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.position.entity import Position
from modules.position.model import PositionInsertRequest, PositionUpdateRequest

router = APIRouter(prefix="/position", tags=["position"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Position).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Position).query.filter(Position.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    return item


@router.post("")
def create(req: PositionInsertRequest, db: Session = Depends(get_db)):
    item = Position(**req.dict())
    db.add(item)
    db.commit()
    return "item created"


@router.put("/{item_id}")
def update(item_id: int, item: PositionUpdateRequest, db: Session = Depends(get_db)):
    item = db.query(Position).query.filter(Position.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    item.name = item.name
    item.company_id = item.company_id
    db.commit()
    return "item updated"


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Position).query.filter(Position.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    db.delete(item)
    db.commit()
    return "item deleted"
