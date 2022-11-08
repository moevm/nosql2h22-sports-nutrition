from datetime import datetime

from bson import ObjectId

from server.data.database.branch_entity import SalaryChangeEntity, VacationEntity, EmployeeEntity, BranchEntity, \
    StockEntity, ProductEntity, ProductDescriptorEntity
from server.data.services.branch.branch import SalaryChange, Vacation


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


def from_salary_change_entity(change: SalaryChangeEntity) -> SalaryChange:
    entity = SalaryChange()
    entity.salary_before = change.salary_before
    entity.salary_after = change.salary_after
    entity.date = change.date
    return entity


def from_vacation_entity(vacation: VacationEntity) -> Vacation:
    entity = Vacation()
    entity.payments = vacation.payments
    entity.start_date = vacation.start_date
    entity.end_date = vacation.end_date
    return entity


def from_employee_entity(employee: EmployeeEntity) -> EmployeeIndexed:
    internal = EmployeeIndexed()
    internal.id = employee.id
    internal.name = employee.name
    internal.surname = employee.surname
    internal.patronymic = employee.patronymic
    internal.passport = employee.passport
    internal.phone = employee.phone
    internal.role = employee.role
    internal.city = employee.city
    internal.employment_date = employee.employment_date
    internal.dismissal_date = employee.dismissal_date
    internal.salary = employee.salary
    internal.shifts_history = employee.shifts_history
    internal.vacation_history = list(map(from_vacation_entity, employee.vacation_history))
    internal.salary_change_history = list(map(from_salary_change_entity, employee.salary_change_history))
    return internal


def from_product_descriptor_entity(descriptor: ProductDescriptorEntity) -> ProductDescriptorIndexed:
    internal = ProductDescriptorIndexed()
    internal.id = descriptor.id
    internal.name = descriptor.name
    return internal


def from_product_entity(product: ProductEntity) -> ProductIndexed:
    internal = ProductIndexed()
    internal.id = product.id
    internal.supplier_id = product.supplier_id
    internal.price = product.price
    internal.descriptor = from_product_descriptor_entity(product.descriptor)
    return internal


def from_stock_entity(stock: StockEntity) -> StockIndexed:
    internal = StockIndexed()
    internal.id = stock.id
    internal.amount = stock.amount
    internal.price = stock.price
    internal.product = from_product_entity(stock.product)
    return internal


def from_branch_entity(branch: BranchEntity) -> BranchIndexed:
    internal = BranchIndexed()
    internal.id = branch.id
    internal.name = branch.name
    internal.city = branch.city
    internal.employees = list(map(from_employee_entity, branch.employees))
    internal.stocks = list(map(from_stock_entity, branch.stocks))
    return internal
