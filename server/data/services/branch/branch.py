from dataclasses import dataclass
from datetime import datetime

from bson import ObjectId


@dataclass
class SalaryChange:
    salary_before: float
    salary_after: float
    date: datetime


@dataclass
class Vacation:
    payments: float
    start_date: datetime
    end_date: datetime


@dataclass
class Employee:
    name: str
    surname: str
    patronymic: str
    passport: str
    phone: str
    role: str
    city: str
    employment_date: datetime
    dismissal_date: datetime
    salary: float
    shifts_history: list
    vacation_history: list
    salary_change_history: list


@dataclass
class InsertBranch:
    name: str
    city: str


@dataclass
class AddProduct:
    product_id: ObjectId
    price: float
    amount: int
