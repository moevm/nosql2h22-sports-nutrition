from typing import List

from pydantic import BaseModel, validator, Field


class SalaryChangeDto(BaseModel):
    salary_before: int = Field(..., description="Salary before must be a non-negative value", gt=0)
    salary_after: int = Field(..., description="Salary after must be a non-negative value", gt=0)
    date: str


class VacationDto(BaseModel):
    payments: int = Field(..., description="Payments must be a non-negative value", gt=0)
    start_date: str
    end_date: str


def check(argument, predicate, message):
    if not predicate(argument):
        raise ValueError(message)
    return argument


class EmployeeDto(BaseModel):
    name: str = Field(..., max_length=30)
    surname: str = Field(..., max_length=30)
    patronymic: str = Field(..., max_length=30)
    passport: str = Field(..., max_length=30)
    phone: str = Field(..., max_length=30)
    role: str = Field(..., max_length=30)
    city: str = Field(..., max_length=30)
    employment_date: str = Field(..., max_length=30)
    dismissal_date: str = Field(..., max_length=30)
    salary: int = Field(..., description="Salary must be a non-negative value", gt=0)
    shifts_history: List[str] = []
    vacation_history: List[VacationDto] = []
    salary_change_history: List[SalaryChangeDto] = []

    @validator('name')
    def name_contains_only_letters(cls, name):
        return check(name, lambda string: string.isalpha(), "Name must contain only alphabetic symbols")

    @validator('surname')
    def surname_contains_only_letters(cls, surname):
        return check(surname, lambda string: string.isalpha(), "Surname must contain only alphabetic symbols")

    @validator('city')
    def city_contains_only_letters(cls, city):
        return check(city, lambda string: string.isalpha(), "City must contain only alphabetic symbols")

    @validator('role')
    def role_contains_only_letters(cls, role):
        return check(role, lambda string: string.isalpha(), "Role must contain only alphabetic symbols")

    @validator('patronymic')
    def patronymic_contains_only_letters(cls, surname):
        return check(surname, lambda string: string.isalpha(), "Patronymic must contain only alphabetic symbols")

    @validator('phone')
    def valid_phone(cls, phone):
        return check(phone, lambda string: string.isnumeric(), "Phone must contain only 0-9 symbols")
