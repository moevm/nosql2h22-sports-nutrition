from dataclasses import dataclass
from datetime import datetime

from bson import ObjectId

from server.common.monad import Optional


@dataclass
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

    def get_dismissal_date(self) -> Optional:
        return Optional(self.dismissal_date)

@dataclass
class ProductDescriptorIndexed:
    id: ObjectId
    name: str


@dataclass
class ProductIndexed:
    id: ObjectId
    descriptor: ProductDescriptorIndexed
    supplier_id: ObjectId
    price: float


@dataclass
class StockIndexed:
    id: ObjectId
    amount: int
    price: float
    product: ProductIndexed


@dataclass
class Branch:
    name: str
    city: str
    stocks: list
    employees: list


@dataclass
class BranchIndexed:
    id: ObjectId
    name: str
    city: str
    stocks: list
    employees: list


@dataclass
class BranchInfo:
    id: ObjectId
    name: str
    city: str
    employees: int
    stocks: int
