from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from model.clinic import Create_Clinic
from engine.fastapi_engine import Base, engine, SessionLocal
from typing import Annotated
from table.tables import Clinic

Base.metadata_create_all(bind=engine)

router = APIRouter(prefix="/clinic", tags=['Clinic'])


def connection_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_Session = Annotated[Session, Depends(connection_db)]


@router.post('/create-clinic', status_code=status.HTTP_201_CREATED)
async def create_clinic(request: Create_Clinic, db: db_Session):
    try:
        clinic_create = Clinic(**request.dict())
        db.add(clinic_create)
        db.commit()
        db.refresh(clinic_create)
        return clinic_create
    except Exception:
        raise HTTPException(status_code=403,detail="Clinic is not created!!")
