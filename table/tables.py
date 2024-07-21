from engine.fastapi_engine import Base
from sqlalchemy import Column, Integer, String, Date, CheckConstraint


class Patient(Base):
    __tablename__ = "Patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(225))
    last_name = Column(String(225))
    DOB = Column(Date)


'''
The Column class in SQLAlchemy defines the datatype, nullability, and other basic properties of the column. 
However, it does not directly support range constraints like gt and lt.
'''


class Doctor(Base):
    __tablename__ = 'Doctors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    degree = Column(String(225), nullable=False)
    specilization = Column(String(225), nullable=False)
    rating = Column(Integer, nullable=False)
    __table_args__ = (
        CheckConstraint('rating > 0 AND rating <= 5', name='rating_check'),
    )


class Clinic(Base):
    __tablename__ = 'Clinic'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    address = Column(String(225), nullable=False)
