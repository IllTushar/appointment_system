from pydantic import BaseModel


class Create_Doctors(BaseModel):
    first_name: str
    last_name: str
    degree: str
    specilization: str
    rating: int


class Doctor_Response(BaseModel):
    id: int
    first_name: str
    last_name: str
    degree: str
    specilization: str
    rating: int

    class Config:
        orm_mode = True
