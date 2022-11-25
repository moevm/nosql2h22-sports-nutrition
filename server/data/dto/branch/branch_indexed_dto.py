from typing import List

from pydantic import BaseModel, Field, validator

from server.data.dto.branch.branch_dto import VacationDto, SalaryChangeDto
from server.data.dto.common.constant import DtoConstant
from server.data.dto.common.util import check


class EmployeeIndexedDto(BaseModel):
    id: str = Field(alias='_id')
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
    salary: float = Field(..., ge=0)
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


class ProductDescriptorIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)


class ProductIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    price: float = Field(..., gt=0)
    descriptor: ProductDescriptorIndexedDto = Field(...)
    supplier_id: str


class StockIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    amount: int = Field(..., gt=0)
    price: float = Field(..., gt=0)
    product: ProductIndexedDto


class BranchInfoDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    city: str


class BranchIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    city: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    stocks: List[StockIndexedDto] = []
    employees: List[EmployeeIndexedDto] = []


class BranchDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    city: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    stocks: List[StockIndexedDto] = []
    employees: List[EmployeeIndexedDto] = []


class IndexedBranchesDto(BaseModel):
    branches: List[BranchDto] = []
