from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.company.entity import company
from modules.company.model import companyInsertRequest, companyUpdateRequest

router=APIRouter(prefix="/company",tags=["company"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(company).all();#    return"read all admin"

@router.post("/create")
def create(req: companyInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    company = company(**req.dict())
    db.add(company)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: companyUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(company).filter(company.id==item_id).first()
    if olderItem is None:
        return "company not found"
    else:
        olderItem.number=req.number
        olderItem.name=req.name
        olderItem.companyid=req.companyid
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    company = db.query(company).filter(company.id == item_id).first()
    if company is None:
        return "company not found"
    else:
        db.delete(company)
        db.commit()
        return "delete successful"