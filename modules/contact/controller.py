from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.contact.entity import Contact
from modules.contact.model import ContactInsertRequest, ContactUpdateRequest


router = APIRouter(prefix="/contact", tags=["contact"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Contact).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Contact).query.filter(Contact.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    return item


@router.post("")
def create(req: ContactInsertRequest, db: Session = Depends(get_db)):
    item = Contact(**req.dict())
    db.add(item)
    db.commit()
    return "item created"


@router.put("/{item_id}")
def update(item_id: int, item: ContactUpdateRequest, db: Session = Depends(get_db)):
    item = db.query(Contact).query.filter(Contact.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    item.firstname = item.firstname
    item.lastname = item.lastname
    item.position_id = item.position_id
    db.commit()
    return "item updated"


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Contact).query.filter(Contact.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    db.delete(item)
    db.commit()
    return "item deleted"
