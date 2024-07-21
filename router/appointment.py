from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from model.appointment import CreateAppointment, ResponseAppointment
from engine.fastapi_engine import Base, engine, SessionLocal
from typing import Annotated
from table.tables import Appointment, Clinic, Patient, Doctor

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/appointment', tags=['Appointment'])


def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_Session = Annotated[Session, Depends(connect_db)]


@router.post('/create-appointment', status_code=status.HTTP_201_CREATED, response_model=ResponseAppointment)
async def create_new_appointment(request: CreateAppointment, db: db_Session):
    # Check if the patient, doctor, and clinic exist
    patient = db.query(Patient).filter(Patient.id == request.patient_id).first()
    doctor = db.query(Doctor).filter(Doctor.id == request.doctor_id).first()
    clinic = db.query(Clinic).filter(Clinic.id == request.clinic_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")

    try:
        new_appointment = Appointment(**request.dict())
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        return new_appointment
    except Exception as e:
        db.rollback()  # Rollback the session in case of error
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/get-all-appointment", status_code=status.HTTP_200_OK)
async def all_appointment(db: db_Session):
    appointments = db.query(Appointment).all()
    if appointments is None:
        raise HTTPException(status_code=404, detail="Appointment is not found!!")
    else:
        return {"data": appointments}
