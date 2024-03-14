from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.email.entity import Email
from modules.email.model import EmailInsertRequest, EmailUpdateRequest

router = APIRouter(prefix="/email", tags=["email"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Email).all()


@router.get("contact_id/{contact_id}")
def get(contact_id: int, db: Session = Depends(get_db)):
    return db.query(Email).filter(Email.contact_id == contact_id).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Email).query.filter(Email.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    return item


@router.post("")
def create(req: EmailInsertRequest, db: Session = Depends(get_db)):
    item = Email(**req.dict())
    db.add(item)
    db.commit()
    return "item created"


@router.put("/{item_id}")
def update(item_id: int, item: EmailUpdateRequest, db: Session = Depends(get_db)):
    item = db.query(Email).query.filter(Email.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    item.mail = item.mail
    item.email = item.email
    item.contact_id = item.contact_id
    db.commit()
    return "item updated"


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Email).query.filter(Email.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    db.delete(item)
    db.commit()
    return "item deleted"
