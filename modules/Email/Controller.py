from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db, SessionLocal
from modules.Email.model import EmailInsertRequest,EmailListResponse, EmailUpdateRequest
from modules.Email.entity import Email

router = APIRouter(prefix="/Email", tags=["Email"])


@router.get("/read/")
def get(db: Session = Depends(get_db)):
    emails = db.query(Email).all()
    return emails


@router.post("/create/")
def create(request: EmailInsertRequest, db: Session = Depends(get_db)):
    item = Email(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/update/{item_id}")
def update(item_id: int, request: EmailUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Email).filter(Email.id == item_id).first()
    if old_item:
        old_item.namelocation = request.namelocation
        old_item.mails = request.mails
        old_item.status = request.status
        old_item.contactId = request.contactId
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "Item not found"}

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Email).filter(Email.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}
