from typing import List, Optional, Any

from pydantic import BaseModel, validator, Field

from server.data.dto.constant import DtoConstant


def check(argument, predicate, message):
    if not predicate(argument):
        raise ValueError(message)
    return argument


class AddProductDto(BaseModel):
    product_id: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    price: float = Field(..., description="Price must be a non-negative value", gt=0)
    amount: int = Field(..., description="Amount must be positive value", ge=0)


class BranchQueryDto(BaseModel):
    name: Optional[Any] = None
    city: Optional[Any] = None
    id: Any = Field(None, alias="_id")


class SalaryChangeDto(BaseModel):
    salary_before: float = Field(..., description="Salary before must be a non-negative value", gt=0)
    salary_after: float = Field(..., description="Salary after must be a non-negative value", gt=0)
    date: str


class VacationDto(BaseModel):
    payments: float = Field(..., description="Payments must be a non-negative value", gt=0)
    start_date: str
    end_date: str


class InsertEmployeeDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    surname: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    patronymic: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    passport: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    phone: str = Field(..., regex=DtoConstant.PHONE_REGEX, min_length=DtoConstant.MIN_STRING_SIZE,
                       max_length=DtoConstant.MAX_STRING_SIZE)
    role: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    city: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    employment_date: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    dismissal_date: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    salary: float = Field(..., description="Salary must be a non-negative value", gt=0)
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
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    city: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
