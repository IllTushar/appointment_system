from pydantic import BaseModel


class Create_Patient(BaseModel):
    first_name: str
    last_name: str
    DOB: str


class Patient_Response(BaseModel):
    id: int
    first_name: str
    last_name: str
    DOB: str

    class Config:
        orm_mode = True
