from pickle import NONE
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.Company.Entity import Company
from modules.Company.Model import CompanyInsertRequest, CompanyUpdateRequest


router = APIRouter(prefix="/Company", tags=["Company"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Company).all()


@router.post("/create")
def creat(req: CompanyInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    item = Company(**req.dict())
    db.add(item)
    db.commit()
    return "inserted"

@router.put("/update/{item_id}")
def update(
    item_id: int,req:CompanyUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Company).filter(Company.id == item_id).first()
    if oldItem is None:
        return "Company not Found"
    else:
        oldItem.name= req.name
        oldItem.address = req.address
        db.commit()
        return "Update Successfull"
    
@router.delete("/dlete/{item_id}")
def delete(
    item_id: int, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Company).filter(Company.id == item_id).first()
    if oldItem is None:
        return "Company not found"
    else : 
        db.delete(oldItem)
        db.commit()
        return "Company has deleted"