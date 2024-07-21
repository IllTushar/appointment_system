from fastapi import FastAPI
from router import patient, doctor

app = FastAPI()

app.include_router(patient.router)
app.include_router(doctor.router)
