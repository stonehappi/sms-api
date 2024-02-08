
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.staff.entity import Staff


router = APIRouter(prefix="/staff", tags=["staff"])


@router.get("/read")
def gets(db: SessionLocal = Depends(get_db)):
    return db.query(Staff).all()

@router.get("/create")
def create():
    return "create new staff"

@router.get("/update")
def update():
    return "update staff"

@router.get("/delete")
def delete():
    return "detele staff"