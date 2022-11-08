from server.data.datetime_formatter import get_string
from server.data.dto.branch.branch_dto import SalaryChangeDto, VacationDto
from server.data.dto.branch.branch_indexed_dto import EmployeeIndexedDto, ProductDescriptorIndexedDto, ProductIndexedDto, \
    StockIndexedDto, BranchIndexedDto
from server.data.services.branch.branch import SalaryChange, Vacation
from server.data.services.branch.branch_indexed import EmployeeIndexed, ProductDescriptorIndexed, ProductIndexed, StockIndexed, \
    BranchIndexed


def dto_from_salary_change(change: SalaryChange) -> SalaryChangeDto:
    entity = SalaryChangeDto.construct()
    entity.salary_before = change.salary_before
    entity.salary_after = change.salary_after
    entity.date = get_string(change.date)
    return entity


def dto_from_vacation(vacation: Vacation) -> VacationDto:
    entity = VacationDto.construct()
    entity.payments = vacation.payments
    entity.start_date = get_string(vacation.start_date)
    entity.end_date = get_string(vacation.end_date)
    return entity


def dto_indexed_from_employee_indexed(employee: EmployeeIndexed) -> EmployeeIndexedDto:
    entity = EmployeeIndexedDto.construct()
    entity.id = str(employee.id)
    entity.name = employee.name
    entity.surname = employee.surname
    entity.patronymic = employee.patronymic
    entity.passport = employee.passport
    entity.phone = employee.phone
    entity.role = employee.role
    entity.city = employee.city
    entity.employment_date = get_string(employee.employment_date)
    entity.dismissal_date = get_string(employee.dismissal_date)
    entity.salary = employee.salary
    entity.shifts_history = list(map(get_string, employee.shifts_history))
    entity.vacation_history = list(map(dto_from_vacation, employee.vacation_history))
    entity.salary_change_history = list(map(dto_from_salary_change, employee.salary_change_history))
    return entity


def dto_indexed_from_product_descriptor_indexed(descriptor: ProductDescriptorIndexed) -> ProductDescriptorIndexedDto:
    internal = ProductDescriptorIndexedDto.construct()
    internal.id = str(descriptor.id)
    internal.name = descriptor.name
    return internal


def dto_indexed_from_product_indexed(product: ProductIndexed) -> ProductIndexedDto:
    internal = ProductIndexedDto.construct()
    internal.id = str(product.id)
    internal.supplier_id = str(product.supplier_id)
    internal.price = product.price
    internal.descriptor = dto_indexed_from_product_descriptor_indexed(product.descriptor)
    return internal


def dto_indexed_from_stock_indexed(stock: StockIndexed) -> StockIndexedDto:
    internal = StockIndexedDto.construct()
    internal.id = str(stock.id)
    internal.amount = stock.amount
    internal.price = stock.price
    internal.product = dto_indexed_from_product_indexed(stock.product)
    return internal


def dto_indexed_from_branch_indexed(branch: BranchIndexed) -> BranchIndexedDto:
    internal = BranchIndexedDto.construct()
    internal.id = str(branch.id)
    internal.name = branch.name
    internal.city = branch.city
    internal.employees = list(map(dto_indexed_from_employee_indexed, branch.employees))
    internal.stocks = list(map(dto_indexed_from_stock_indexed, branch.stocks))
    return internal
