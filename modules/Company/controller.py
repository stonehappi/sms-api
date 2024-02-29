from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Company.entity import Company
from modules.Company.model import CompanyInsertRequest, CompanyListResponse, CompanyUpdateRequest, CompanyDeleteRequest

router = APIRouter(prefix="/Company", tags=["Company"])


@router.get("/read")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Company).filter(Company.id == item_id).first()
    if item:
        return item
    return {"message": "Item not found"}


@router.post("/Company/{item_id}")
def create(request: CompanyInsertRequest, db: Session = Depends(get_db)):
    item = Company(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.put("/Company/{item_id}")
def update(item_id: int, request: CompanyUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Company).filter(Company.id == item_id).first()
    if old_item:
        old_item.update(request.dict())
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "Item not found"}

@router.delete("/Company/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Company).filter(Company.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}