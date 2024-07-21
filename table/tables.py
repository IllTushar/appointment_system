from engine.fastapi_engine import Base
from sqlalchemy import Column, Integer, String, Date, CheckConstraint, Time, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Patient(Base):
    __tablename__ = "Patients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(225))
    last_name = Column(String(225))
    DOB = Column(Date)
    appointment = relationship('Appointment', back_populates='patient')


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
    appointment = relationship('Appointment', back_populates='doctor')


class Clinic(Base):
    __tablename__ = 'Clinic'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(225), nullable=False)
    address = Column(String(225), nullable=False)
    appointment = relationship('Appointment', back_populates='clinic')


class Appointment(Base):
    __tablename__ = 'Appointments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    arrival_time = Column(Time, nullable=False)
    complete_time = Column(Time)
    active = Column(Boolean, default=True)
    patient_id = Column(Integer, ForeignKey('Patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('Doctors.id'), nullable=False)
    clinic_id = Column(Integer, ForeignKey('Clinic.id'), nullable=False)
    patient = relationship('Patient', back_populates='appointment')
    doctor = relationship('Doctor', back_populates='appointment')
    clinic = relationship('Clinic', back_populates='appointment')
