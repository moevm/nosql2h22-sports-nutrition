from dataclasses import dataclass
from typing import List, Optional, Any

from pydantic import BaseModel, validator, Field


@dataclass
class DtoConstant:
    STRING_SIZE: int = 30


def check(argument, predicate, message):
    if not predicate(argument):
        raise ValueError(message)
    return argument


class BranchQueryDto(BaseModel):
    name: Optional[Any] = None
    city: Optional[Any] = None
    id: Any = Field(None, alias="_id")


class SalaryChangeDto(BaseModel):
    salary_before: int = Field(..., description="Salary before must be a non-negative value", gt=0)
    salary_after: int = Field(..., description="Salary after must be a non-negative value", gt=0)
    date: str


class VacationDto(BaseModel):
    payments: int = Field(..., description="Payments must be a non-negative value", gt=0)
    start_date: str
    end_date: str


class InsertEmployeeDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    surname: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    patronymic: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    passport: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    phone: str = Field(..., regex=r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$")
    role: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    city: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    employment_date: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    dismissal_date: str = Field(..., max_length=DtoConstant.STRING_SIZE)
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

    @validator('patronymic')
    def patronymic_contains_only_letters(cls, surname):
        return check(surname, lambda string: string.isalpha(), "Patronymic must contain only alphabetic symbols")


class InsertBranchDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    city: str = Field(..., max_length=DtoConstant.STRING_SIZE)
