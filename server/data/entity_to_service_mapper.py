from server.data.database.branch_entity import SalaryChangeEntity, VacationEntity, EmployeeEntity, \
    ProductDescriptorEntity, ProductEntity, StockEntity, BranchEntity, BranchInfoEntity
from server.data.database.supplier_entity import SupplierEntity, SupplierInfoEntity
from server.data.database.sale_entity import SaleEntity
from server.data.services.branch.branch import SalaryChange, Vacation
from server.data.services.branch.branch_indexed import EmployeeIndexed, ProductDescriptorIndexed, ProductIndexed, \
    StockIndexed, BranchIndexed, BranchInfo
from server.data.services.supplier.supplier import SupplierIndexed, SupplierInfo
from server.data.services.sale.sale import SaleIndexed

from logging import info

def from_salary_change_entity(change: SalaryChangeEntity) -> SalaryChange:
    return SalaryChange(change.salary_before, change.salary_after, change.date)


def from_supplier_entity_to_indexed(supplier: SupplierEntity) -> SupplierIndexed:
    return SupplierIndexed(supplier.id, supplier.name, supplier.email, supplier.phone,
                           list(map(from_product_entity, supplier.products)))


def from_supplier_entity_to_info(supplier: SupplierInfoEntity) -> SupplierInfo:
    return SupplierInfo(supplier.id, supplier.name, supplier.email, supplier.phone, supplier.products)


def from_vacation_entity(vacation: VacationEntity) -> Vacation:
    return Vacation(vacation.payments, vacation.start_date, vacation.end_date)


def from_employee_entity(employee: EmployeeEntity) -> EmployeeIndexed:
    return EmployeeIndexed(employee.id, employee.name, employee.surname, employee.patronymic, employee.passport,
                           employee.phone, employee.role, employee.city, employee.employment_date,
                           employee.dismissal_date, employee.salary, employee.shifts_history,
                           list(map(from_vacation_entity, employee.vacation_history)),
                           list(map(from_salary_change_entity, employee.salary_change_history)))


def from_product_descriptor_entity(descriptor: ProductDescriptorEntity) -> ProductDescriptorIndexed:
    return ProductDescriptorIndexed(descriptor.id, descriptor.name)


def from_product_entity(product: ProductEntity) -> ProductIndexed:
    return ProductIndexed(product.id, from_product_descriptor_entity(product.descriptor), product.supplier_id,
                          product.price)


def from_stock_entity(stock: StockEntity) -> StockIndexed:
    return StockIndexed(stock.id, stock.amount, stock.price, from_product_entity(stock.product))


def from_branch_entity(branch: BranchEntity) -> BranchIndexed:
    return BranchIndexed(branch.id, branch.name, branch.city, list(map(from_stock_entity, branch.stocks)),
                         list(map(from_employee_entity, branch.employees)))


def from_branch_entity_to_info(branch: BranchInfoEntity) -> BranchInfo:
    return BranchInfo(branch.id, branch.name, branch.city, branch.employees, branch.stocks)


def from_sale_entity(sale: SaleEntity) -> SaleIndexed:
    return SaleIndexed(sale.id, str(sale.supplier_id), str(sale.product_id),
                       str(sale.branch_id), sale.price, sale.amount)
