from server.common.logger import is_logged
from server.data.datetime_formatter import get_string
from server.data.dto.branch.branch_dto import SalaryChangeDto, VacationDto
from server.data.dto.branch.branch_indexed_dto import EmployeeIndexedDto, ProductDescriptorIndexedDto, \
    ProductIndexedDto, \
    StockIndexedDto, BranchInfoDto, BranchIndexedDto
from server.data.dto.supplier.supplier_indexed_dto import SupplierIndexedDto, SupplierInfoDto
from server.data.services.branch.branch import SalaryChange, Vacation
from server.data.services.branch.branch_indexed import EmployeeIndexed, ProductDescriptorIndexed, ProductIndexed, \
    StockIndexed, \
    BranchIndexed, BranchInfo
from server.data.services.supplier.supplier import SupplierIndexed, SupplierInfo
from server.data.services.sale.sale import SaleIndexed
from server.data.dto.sale.sale_indexed_dto import SaleIndexedDto


@is_logged(['document'])
def dto_from_salary_change(change: SalaryChange) -> SalaryChangeDto:
    dto = SalaryChangeDto.construct()
    dto.salary_before = change.salary_before
    dto.salary_after = change.salary_after
    dto.date = get_string(change.date)
    return dto


@is_logged(['document'])
def dto_from_vacation(vacation: Vacation) -> VacationDto:
    dto = VacationDto.construct()
    dto.payments = vacation.payments
    dto.start_date = get_string(vacation.start_date)
    dto.end_date = get_string(vacation.end_date)
    return dto


@is_logged(['document'])
def dto_indexed_from_employee_indexed(employee: EmployeeIndexed) -> EmployeeIndexedDto:
    dto = EmployeeIndexedDto.construct()
    dto.id = str(employee.id)
    dto.name = employee.name
    dto.surname = employee.surname
    dto.patronymic = employee.patronymic
    dto.passport = employee.passport
    dto.phone = employee.phone
    dto.role = employee.role
    dto.city = employee.city
    dto.employment_date = get_string(employee.employment_date)
    dto.dismissal_date = get_string(employee.dismissal_date)
    dto.salary = employee.salary
    dto.shifts_history = list(map(get_string, employee.shifts_history))
    dto.vacation_history = list(map(dto_from_vacation, employee.vacation_history))
    dto.salary_change_history = list(map(dto_from_salary_change, employee.salary_change_history))
    return dto


@is_logged(['document'])
def dto_indexed_from_product_descriptor_indexed(descriptor: ProductDescriptorIndexed) -> ProductDescriptorIndexedDto:
    dto = ProductDescriptorIndexedDto.construct()
    dto.id = str(descriptor.id)
    dto.name = descriptor.name
    return dto


@is_logged(['document'])
def dto_indexed_from_product_indexed(product: ProductIndexed) -> ProductIndexedDto:
    dto = ProductIndexedDto.construct()
    dto.id = str(product.id)
    dto.supplier_id = str(product.supplier_id)
    dto.price = product.price
    dto.descriptor = dto_indexed_from_product_descriptor_indexed(product.descriptor)
    return dto


@is_logged(['document'])
def dto_indexed_from_stock_indexed(stock: StockIndexed) -> StockIndexedDto:
    dto = StockIndexedDto.construct()
    dto.id = str(stock.id)
    dto.amount = stock.amount
    dto.price = stock.price
    dto.product = dto_indexed_from_product_indexed(stock.product)
    return dto


@is_logged(['document'])
def dto_indexed_from_branch_indexed(branch: BranchIndexed) -> BranchIndexedDto:
    dto = BranchIndexedDto.construct()
    dto.id = str(branch.id)
    dto.name = branch.name
    dto.city = branch.city
    dto.employees = list(map(dto_indexed_from_employee_indexed, branch.employees))
    dto.stocks = list(map(dto_indexed_from_stock_indexed, branch.stocks))
    return dto


@is_logged(['document'])
def dto_info_from_branch_info(branch: BranchInfo) -> BranchInfoDto:
    dto = BranchInfoDto.construct()
    dto.id = str(branch.id)
    dto.name = branch.name
    dto.city = branch.city
    dto.employees = branch.employees
    dto.stocks = branch.stocks
    return dto


@is_logged(['document'])
def dto_indexed_from_supplier(supplier: SupplierIndexed) -> SupplierIndexedDto:
    dto = SupplierIndexedDto.construct()
    dto.id = str(supplier.id)
    dto.name = supplier.name
    dto.email = supplier.email
    dto.phone = supplier.phone
    dto.products = list(map(dto_indexed_from_product_indexed, supplier.products))
    return dto


@is_logged(['document'])
def dto_info_from_supplier(supplier: SupplierInfo) -> SupplierInfoDto:
    dto = SupplierInfoDto.construct()
    dto.id = str(supplier.id)
    dto.name = supplier.name
    dto.email = supplier.email
    dto.phone = supplier.phone
    dto.products = supplier.products
    return dto


@is_logged(['document'])
def dto_indexed_from_sale_indexed(sale: SaleIndexed) -> SaleIndexedDto:
    dto = SaleIndexedDto.construct()
    dto.id = str(sale.id)
    dto.supplier_id = str(sale.supplier_id)
    dto.product_id = str(sale.product_id)
    dto.branch_id = str(sale.branch_id)
    dto.price = sale.price
    dto.amount = sale.amount

    return dto
