from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from model.doctors import Create_Doctors
from engine.fastapi_engine import Base, engine, SessionLocal
from typing import Annotated
from table.tables import Doctor

Base.metadata.create_all(bind=engine)
router = APIRouter(prefix='/doctor',tags=['Doctor'])


def connection_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_Session = Annotated[Session, Depends(connection_db)]


@router.post("/create-doctor", status_code=status.HTTP_201_CREATED)
async def create_doctor(request: Create_Doctors, db: db_Session):
    try:
        data = Doctor(**request.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception:
        raise HTTPException(status_code=403, detail="Data is not created!!")


@router.get("/get-all-doctors", status_code=status.HTTP_200_OK)
async def get_all_doctors(db: db_Session):
    details = db.query(Doctor).all()
    if details is None:
        raise HTTPException(status_code=404, detail="details not found")
    else:
        return {"data": details}
