from pydantic import BaseModel
from datetime import time, date
from typing import Optional


class CreateAppointment(BaseModel):
    appointment_date: date
    appointment_time: time
    arrival_time: time
    complete_time: Optional[time] = None
    active: bool
    patient_id: int
    doctor_id: int
    clinic_id: int


class ResponseAppointment(BaseModel):
    id: int
    appointment_date: date
    appointment_time: time
    arrival_time: time
    complete_time: Optional[time] = None
    active: bool
    patient_id: int
    doctor_id: int
    clinic_id: int

    class Config:
        orm_mode = True
