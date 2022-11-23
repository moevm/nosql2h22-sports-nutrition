from datetime import datetime
from logging import info
from typing import List

from pydantic import BaseModel, Field

from server.data.database.common import PydanticObjectId


class SalaryChangeEntity(BaseModel):
    salary_before: float
    salary_after: float
    date: datetime


class VacationEntity(BaseModel):
    payments: float
    start_date: datetime
    end_date: datetime


class EmployeeEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
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
    vacation_history: List[VacationEntity]
    salary_change_history: List[SalaryChangeEntity]


class ProductDescriptorEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    name: str


class ProductEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    descriptor: ProductDescriptorEntity
    supplier_id: PydanticObjectId
    price: float


class StockEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    amount: int
    price: float
    product: ProductEntity


class BranchEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    name: str
    city: str
    stocks: List[StockEntity] = []
    employees: List[EmployeeEntity] = []


def from_salary_change_document(document) -> SalaryChangeEntity:
    info(f"parse document: {document}")

    entity = SalaryChangeEntity.construct()
    entity.salary_before = document['salary_before']
    entity.salary_after = document['salary_after']
    entity.date = document['date']
    return entity


def from_vacation_document(document) -> VacationEntity:
    info(f"parse document: {document}")

    entity = VacationEntity.construct()
    entity.payments = document['payments']
    entity.start_date = document['start_date']
    entity.end_date = document['end_date']
    return entity


def from_employee_document(document) -> EmployeeEntity:
    info(f"parse document: {document}")

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


def from_product_descriptor_document(document) -> ProductDescriptorEntity:
    info(f"parse document: {document}")

    entity = ProductDescriptorEntity.construct()
    entity.id = document['_id']
    entity.name = document['name']
    return entity


def from_product_document(document) -> ProductEntity:
    info(f"parse document: {document}")

    entity = ProductEntity.construct()
    entity.id = document['_id']
    entity.supplier_id = document['supplier_id']
    entity.price = document['price']
    entity.descriptor = from_product_descriptor_document(document['descriptor'])
    return entity


def from_stock_document(document) -> StockEntity:
    info(f"parse document: {document}")

    entity = StockEntity.construct()
    entity.id = document['_id']
    entity.amount = document['amount']
    entity.price = document['price']
    entity.product = from_product_document(document['product'])
    return entity


def from_branch_document(document) -> BranchEntity:
    info(f"parse document: {document}")

    entity = BranchEntity.construct()
    entity.id = document['_id']
    entity.name = document['name']
    entity.city = document['city']
    entity.employees = list(map(from_employee_document, document['employees']))
    entity.stocks = list(map(from_stock_document, document['stocks']))
    return entity


def from_branch_info_document(document) -> BranchEntity:
    info(f"parse document: {document}")

    entity = BranchEntity.construct()
    entity.id = document['_id']
    entity.name = document['name']
    entity.city = document['city']
    return entity
