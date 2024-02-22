from datetime import date, datetime, time
from pydantic import BaseModel


class NewStaff_InsertionRequest(BaseModel):
    fullname: str
    age: int
    startdate: date
    salary: float
    #workhour: float
    position: str
    department: str
    location: str
    #attendance_daily: datetime
    email: str
    #login_time: time

class Staff_UpdateRequest(BaseModel):
    salary: float
    position: str
    department: str
    location: str
    email: str

class Staff_SalaryRequest(BaseModel):
    fullname: str
    salary: float
    # workhour: float
    # attendance_daily: datetime
    # login_time: time