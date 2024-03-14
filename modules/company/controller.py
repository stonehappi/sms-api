from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.company.entity import Company
from modules.company.model import CompanyInsertRequest, CompanyUpdateRequest

router = APIRouter(prefix="/company", tags=["company"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Company).all()


@router.get("/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Company).query.filter(Company.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    return item


@router.post("")
def create(req: CompanyInsertRequest, db: Session = Depends(get_db)):
    item = Company(**req.dict())
    db.add(item)
    db.commit()
    return "item created"


@router.put("/{item_id}")
def update(item_id: int, item: CompanyUpdateRequest, db: Session = Depends(get_db)):
    item = db.query(Company).query.filter(Company.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    item.name = item.name
    item.address = item.address
    db.commit()
    return "item updated"


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Company).query.filter(Company.id == item_id).first()
    if item is None:
        return f"item id = {item_id} not found"
    db.delete(item)
    db.commit()
    return "item deleted"
