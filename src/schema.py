from pydantic import BaseModel
from fastapi import FastAPI
from uuid import UUID
from datetime import datetime
from datetime import date


class MedicalExamination(BaseModel):
    date_time: datetime
    doctor: str
    report: str


class Owner(BaseModel):
    name: str


class Pet(BaseModel):
    id: UUID
    name: str
    birthday: date
    kind: str
    owner: Owner
    medical_exam: list[MedicalExamination]


class PetResponse(BaseModel):
    pet:Pet
