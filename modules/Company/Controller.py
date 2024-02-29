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
def creat(req: CompanyInsertRequest):
    return req

@router.put("/update/{item_id}")
def update(
    item_id: int,req:CompanyUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Company).filter(Company.id == item_id).first()
    if oldItem is None:
        return "Company not Found"
    else:
        oldItem.floor= req.floor
        oldItem.room = req.room
        oldItem.short_name = req.short_name
        db.commit()
        return "Update Successfull"
    
@router.get("/dlete/{item_id}")
def delete(
    item_id: int,req:CompanyUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Company).filter(Company.id == item_id).first()
    if oldItem is NONE:
        return "Company not found"
    else : 
        db.delete(oldItem)
        db.comit()
        return "Company has deleted"