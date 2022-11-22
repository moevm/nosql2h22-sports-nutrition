from datetime import datetime

from bson import ObjectId


class EmployeeIndexed:
    id: ObjectId
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


class ProductDescriptorIndexed:
    id: ObjectId
    name: str


class ProductIndexed:
    id: ObjectId
    descriptor: ProductDescriptorIndexed
    supplier_id: ObjectId
    price: float


class StockIndexed:
    id: ObjectId
    amount: int
    price: float
    product: ProductIndexed


class BranchIndexed:
    id: ObjectId
    name: str
    city: str
    stocks: list
    employees: list
