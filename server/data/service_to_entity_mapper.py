from bson import ObjectId

from server.data.database.branch_entity import EmployeeEntity, SalaryChangeEntity, VacationEntity, BranchEntity, \
    ProductEntity, ProductDescriptorEntity, StockEntity
from server.data.database.supplier_entity import SupplierEntity
from server.data.services.branch.branch import Employee, Vacation, SalaryChange, InsertBranch
from server.data.services.product.product import InsertProductWithDescriptor, ProductDescriptor
from server.data.services.supplier.supplier import InsertSupplier


def entity_from_descriptor(descriptor: ProductDescriptor):
    entity = ProductDescriptorEntity.construct()
    entity.name = descriptor.name
    entity.id = ObjectId()
    return entity


def entity_from_insert_product_with_descriptor(supplier_id: ObjectId,
                                               product: InsertProductWithDescriptor) -> ProductEntity:
    entity = ProductEntity.construct()
    entity.id = ObjectId()
    entity.descriptor = entity_from_descriptor(product.descriptor)
    entity.price = product.price
    entity.supplier_id = supplier_id
    return entity


def entity_from_salary_change(change: SalaryChange) -> SalaryChangeEntity:
    entity = SalaryChangeEntity.construct()
    entity.salary_before = change.salary_before
    entity.salary_after = change.salary_after
    entity.date = change.date
    return entity


def entity_from_vacation(vacation: Vacation) -> VacationEntity:
    entity = VacationEntity.construct()
    entity.payments = vacation.payments
    entity.start_date = vacation.start_date
    entity.end_date = vacation.end_date
    return entity


def entity_from_employee(employee: Employee) -> EmployeeEntity:
    entity = EmployeeEntity.construct()
    entity.id = ObjectId()
    entity.name = employee.name
    entity.surname = employee.surname
    entity.patronymic = employee.patronymic
    entity.passport = employee.passport
    entity.phone = employee.phone
    entity.role = employee.role
    entity.city = employee.city
    entity.employment_date = employee.employment_date
    entity.dismissal_date = employee.dismissal_date
    entity.salary = employee.salary
    entity.shifts_history = employee.shifts_history
    entity.vacation_history = list(map(entity_from_vacation, employee.vacation_history))
    entity.salary_change_history = list(map(entity_from_salary_change, employee.salary_change_history))
    return entity


def entity_from_branch(branch: InsertBranch) -> BranchEntity:
    entity = BranchEntity.construct()
    entity.name = branch.name
    entity.city = branch.city
    return entity


def entity_from_supplier(supplier: InsertSupplier) -> SupplierEntity:
    entity = SupplierEntity.construct()
    entity.name = supplier.name
    entity.email = supplier.email
    entity.phone = supplier.phone
    return entity


def entity_stock_from_product(product: ProductEntity, price: float, amount: int) -> StockEntity:
    entity = StockEntity.construct()
    entity.product = product
    entity.id = ObjectId()
    entity.price = price
    entity.amount = amount
    return entity