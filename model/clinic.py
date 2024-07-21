from pydantic import BaseModel


class Create_Clinic(BaseModel):
    name: str
    address: str


class Response_Clinic(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True
