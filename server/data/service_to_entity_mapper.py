from bson import ObjectId

from server.data.database.branch_entity import EmployeeEntity, SalaryChangeEntity, VacationEntity, BranchEntity, \
    ProductEntity, ProductDescriptorEntity, StockEntity
from server.data.database.supplier_entity import SupplierEntity
from server.data.services.branch.branch import Employee, Vacation, SalaryChange, InsertBranch
from server.data.services.branch.branch_indexed import StockIndexed, ProductIndexed, \
    ProductDescriptorIndexed, EmployeeIndexed, Branch
from server.data.services.product.product import InsertProductWithDescriptor, ProductDescriptor
from server.data.services.supplier.supplier import InsertSupplier, Supplier
from server.data.services.sale.sale import InsertSale
from server.data.database.sale_entity import SaleEntity
from server.data.database.common import PydanticObjectId


def get_descriptor_entity(descriptor, id: ObjectId) -> ProductDescriptorEntity:
    entity = ProductDescriptorEntity.construct()
    entity.name = descriptor.name
    entity.id = id
    return entity


def entity_from_descriptor_indexed(descriptor: ProductDescriptorIndexed) -> ProductDescriptorEntity:
    return get_descriptor_entity(descriptor, descriptor.id)


def entity_from_descriptor(descriptor: ProductDescriptor) -> ProductDescriptorEntity:
    return get_descriptor_entity(descriptor, ObjectId())


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
    return get_employee_entity(employee, ObjectId(), entity_from_vacation, entity_from_salary_change)


def entity_from_employee_indexed(employee: EmployeeIndexed) -> EmployeeEntity:
    return get_employee_entity(employee, employee.id, entity_from_vacation, entity_from_salary_change)


def get_employee_entity(employee, id: ObjectId, vacation_mapper, salary_change_mapper) -> EmployeeEntity:
    entity = EmployeeEntity.construct()
    entity.id = id
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
    entity.vacation_history = list(map(vacation_mapper, employee.vacation_history))
    entity.salary_change_history = list(map(salary_change_mapper, employee.salary_change_history))
    return entity


def entity_from_insert_branch(branch: InsertBranch) -> BranchEntity:
    entity = BranchEntity.construct()
    entity.name = branch.name
    entity.city = branch.city
    return entity


def entity_from_product_indexed(product: ProductIndexed) -> ProductEntity:
    entity = ProductEntity.construct()
    entity.id = product.id
    entity.price = product.price
    entity.descriptor = entity_from_descriptor_indexed(product.descriptor)
    entity.supplier_id = product.supplier_id
    return entity


def entity_from_stock_indexed(stock: StockIndexed) -> StockEntity:
    entity = StockEntity.construct()
    entity.id = stock.id
    entity.price = stock.price
    entity.amount = stock.amount
    entity.product = entity_from_product_indexed(stock.product)
    return entity


def entity_from_branch(branch: Branch) -> BranchEntity:
    entity = BranchEntity.construct()
    entity.name = branch.name
    entity.city = branch.city
    entity.stocks = list(map(entity_from_stock_indexed, branch.stocks))
    entity.employees = list(map(entity_from_employee_indexed, branch.employees))
    return entity


def bson_from_supplier(supplier: Supplier):
    return entity_from_supplier(supplier).dict(by_alias=True)


def bson_from_branch(branch: Branch):
    return entity_from_branch(branch).dict(by_alias=True)


def entity_from_supplier(supplier: Supplier) -> SupplierEntity:
    entity = SupplierEntity.construct()
    entity.name = supplier.name
    entity.email = supplier.email
    entity.phone = supplier.phone
    entity.products = list(map(entity_from_product_indexed, supplier.products))
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


def entity_from_insert_sale(insert_sale: InsertSale) -> SaleEntity:
    entity = SaleEntity.construct()
    entity.id = ObjectId()
    entity.supplier_id = PydanticObjectId(insert_sale.supplier_id)
    entity.product_id = PydanticObjectId(insert_sale.product_id)
    entity.branch_id = PydanticObjectId(insert_sale.branch_id)
    entity.price = insert_sale.price
    entity.amount = insert_sale.amount
    entity.date = insert_sale.date
    return entity
