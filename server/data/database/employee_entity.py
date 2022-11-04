from datetime import datetime
from typing import List

from bson import ObjectId
from pydantic import BaseModel


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class SalaryChangeEntity(BaseModel):
    salary_before: int
    salary_after: int
    date: datetime


class VacationEntity(BaseModel):
    payments: int
    start_date: datetime
    end_date: datetime


class EmployeeEntity(BaseModel):
    id: PydanticObjectId
    name: str
    surname: str
    patronymic: str
    passport: str
    phone: str
    role: str
    city: str
    employment_date: datetime
    dismissal_date: datetime
    salary: int
    shifts_history: list
    vacation_history: List[VacationEntity]
    salary_change_history: List[SalaryChangeEntity]


def from_salary_change_document(document) -> SalaryChangeEntity:
    entity = SalaryChangeEntity.construct()
    entity.salary_before = document['salary_before']
    entity.salary_after = document['salary_after']
    entity.date = document['date']
    return entity


def from_vacation_document(document) -> VacationEntity:
    entity = VacationEntity.construct()
    entity.payments = document['payments']
    entity.start_date = document['start_date']
    entity.end_date = document['end_date']
    return entity


def from_employee_document(document) -> EmployeeEntity:
    entity = EmployeeEntity.construct()
    entity.id = document['_id']
    entity.name = document['name']
    entity.surname = document['surname']
    entity.patronymic = document['patronymic']
    entity.passport = document['passport']
    entity.phone = document['phone']
    entity.role = document['role']
    entity.city = document['city']
    entity.employment_date = document['employment_date']
    entity.dismissal_date = document['dismissal_date']
    entity.salary = document['salary']
    entity.shifts_history = document['shifts_history']
    entity.vacation_history = list(map(from_vacation_document, document['vacation_history']))
    entity.salary_change_history = list(map(from_salary_change_document, document['salary_change_history']))
    return entity
