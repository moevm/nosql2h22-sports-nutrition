from typing import List

from pydantic import BaseModel, Field

from server.data.dto.branch.branch_dto import VacationDto, SalaryChangeDto


class EmployeeIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    surname: str
    patronymic: str
    passport: str
    phone: str
    role: str
    city: str
    employment_date: str
    dismissal_date: str
    salary: float
    shifts_history: List[str]
    vacation_history: List[VacationDto]
    salary_change_history: List[SalaryChangeDto]


class ProductDescriptorIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str


class ProductIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    descriptor: ProductDescriptorIndexedDto
    supplier_id: str
    price: float


class StockIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    amount: int
    price: float
    product: ProductIndexedDto


class BranchInfoDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    city: str


class BranchIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    city: str
    stocks: list
    employees: list
