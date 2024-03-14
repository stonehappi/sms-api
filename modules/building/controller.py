from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.building.entity import Building
from modules.building.model import BuildingInsertRequest, BuildingUpdateRequest

router = APIRouter(prefix="/building", tags=["building"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Building).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Building).query.filter(Building.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    return item


@router.post("")
def create(req: BuildingInsertRequest, db: Session = Depends(get_db)):
    item = Building(**req.dict())
    db.add(item)
    db.commit()
    return "item created"


@router.put("/{item_id}")
def update(item_id: int, item: BuildingUpdateRequest, db: Session = Depends(get_db)):
    item = db.query(Building).query.filter(Building.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    item.name = item.name
    db.commit()
    return "item updated"


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Building).query.filter(Building.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    db.delete(item)
    db.commit()
    return "item deleted"
