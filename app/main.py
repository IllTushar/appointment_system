from fastapi import FastAPI
from router import patient, doctor, clinic

app = FastAPI()

# Patients..
app.include_router(patient.router)

# Doctors
app.include_router(doctor.router)

# Clinic
app.include_router(clinic.router)
