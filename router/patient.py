from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from engine.fastapi_engine import Base, engine
from table.tables import Patient
from engine.fastapi_engine import SessionLocal
from model.patient import Create_Patient
from typing import Annotated

# Create the database tables
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/patient", tags=['Patient'])


def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_Session = Annotated[Session, Depends(connect_db)]


@router.post("/create-patient", status_code=status.HTTP_201_CREATED)
async def create_patient(request: Create_Patient, db: db_Session):
    try:
        create_data = Patient(**request.dict())
        db.add(create_data)
        db.commit()
        db.refresh(create_data)
        return create_data
    except Exception:
        raise HTTPException(status_code=403, detail="Patient is not created!!")


@router.get("/get-all-patient", status_code=status.HTTP_200_OK)
async def get_all_data(db: db_Session):
    get_data = db.query(Patient).all()
    if get_data is None:
        raise HTTPException(status_code=404, detail="Data is not present!!")
    else:
        return {"data": get_data}
