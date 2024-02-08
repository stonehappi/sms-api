from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.user.entity import User
from modules.user.model import UserInsertRequest, UserUpdateRequest

router = APIRouter(prefix="/user", tags=["user"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(User).filter(User.id == item_id).first()
    if item:
        return item
    return {"message": "Item not found"}


@router.post("")
def create(request: UserInsertRequest, db: Session = Depends(get_db)):
    item = User(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{item_id}")
def updae(item_id: int, request: UserUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(User).filter(User.id == item_id).first()
    if old_item:
        for key, value in request.dict().items():
            setattr(old_item, key, value)
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "Item not found"}


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(User).filter(User.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}
