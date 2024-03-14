from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.phone.entity import Phone
from modules.phone.model import PhoneInsertRequest, PhoneUpdateRequest

router = APIRouter(prefix="/phone", tags=["phone"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Phone).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Phone).query.filter(Phone.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    return item


@router.post("")
def create(req: PhoneInsertRequest, db: Session = Depends(get_db)):
    item = Phone(**req.dict())
    db.add(item)
    db.commit()
    return "item created"


@router.put("/{item_id}")
def update(item_id: int, item: PhoneUpdateRequest, db: Session = Depends(get_db)):
    item = db.query(Phone).query.filter(Phone.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    item.number = item.number
    item.phone = item.phone
    item.contact_id = item.contact_id
    db.commit()
    return "item updated"


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Phone).query.filter(Phone.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    db.delete(item)
    db.commit()
    return "item deleted"
