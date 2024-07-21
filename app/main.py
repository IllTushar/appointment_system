from fastapi import FastAPI
from router import patient, doctor, clinic, appointment

app = FastAPI()

# Patients..
app.include_router(patient.router)

# Doctors
app.include_router(doctor.router)

# Clinic
app.include_router(clinic.router)

# Appointment
app.include_router(appointment.router)
