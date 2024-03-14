
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Company.entity import Company
from modules.Company.model import CompanyInsertRequest, CompanyListResponse, CompanyUpdateRequest, CompanyDeleteRequest

router = APIRouter(prefix="/Company", tags=["Company"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    companys = db.query(Company).all()
    return companys


@router.post("/create")
def create(request: CompanyInsertRequest, db: Session = Depends(get_db)):
    item = Company(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return CompanyInsertRequest(**item.__dict__)

@router.put("/update/{item_id}")
def update(item_id: int, request: CompanyUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Company).filter(Company.id == item_id).first()
    if old_item is None:
        # old_item.update(request.dict())
        return {"message": "Item not found"}
    else:
        old_item.name = request.name
        old_item.Address = request.Address
        db.commit()
        db.refresh(old_item)
        return "Updated"
    

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Company).filter(Company.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}