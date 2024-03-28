from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db, SessionLocal
from modules.Company.model import ComapanyUpdateRequest, CompanyInsertRequest
from modules.Company.entity import Company

router = APIRouter(prefix="/Company", tags=["Company"])


@router.get("/read/")
def get(db: Session = Depends(get_db)):
    Companys = db.query(Company).all()
    return Companys


@router.post("/create/")
def create(request:  CompanyInsertRequest, db: Session = Depends(get_db)):
    item = Company(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/update/{item_id}")
def update(item_id: int, request: ComapanyUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Company).filter(Company.id == item_id).first()
    if old_item:
        old_item.name = request.name
        old_item.address = request.address
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "shit your Item not found"}

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Company).filter(Company.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item already deleted successfully"}
    return {"message": "Item cannot found"}