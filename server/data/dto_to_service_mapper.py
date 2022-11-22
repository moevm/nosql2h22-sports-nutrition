from bson import ObjectId

from server.common.exceptions import EmptyQuery
from server.common.monad import Optional
from server.data.database.query import BranchQuery, FieldEqualsValueQueryRepresentation, IdQueryRepresentation, \
    EmployeeInBranchQuery, IntervalQueryRepresentation, IntervalHolder
from server.data.datetime_formatter import get_datetime
from server.data.dto.branch.branch_dto import AddProductDto, SalaryChangeDto, VacationDto, InsertEmployeeDto, \
    InsertBranchDto, BranchQueryDto, EmployeeInBranchQueryDto
from server.data.dto.product.product_dto import ProductDescriptorDto, InsertProductWithDescriptorDto
from server.data.dto.supplier.supplier_dto import InsertSupplierDto
from server.data.services.branch.branch import AddProduct, SalaryChange, Vacation, Employee, InsertBranch
from server.data.services.product.product import ProductDescriptor, InsertProductWithDescriptor
from server.data.services.supplier.supplier import InsertSupplier


def first(elements) -> Optional:
    if elements is not None and len(elements) > 0:
        return Optional(elements[0])
    else:
        return Optional(None)


def from_add_product_dto(request: AddProductDto):
    entity = AddProduct()
    entity.price = request.price
    entity.amount = request.amount
    entity.product_id = ObjectId(request.product_id)
    return entity


def from_salary_change_dto(change: SalaryChangeDto) -> SalaryChange:
    entity = SalaryChange()
    entity.salary_before = change.salary_before
    entity.salary_after = change.salary_after
    entity.date = get_datetime(change.date)
    return entity


def from_vacation_dto(vacation: VacationDto) -> Vacation:
    entity = Vacation()
    entity.payments = vacation.payments
    entity.start_date = get_datetime(vacation.start_date)
    entity.end_date = get_datetime(vacation.end_date)
    return entity


def from_employee_dto(employee: InsertEmployeeDto) -> Employee:
    internal = Employee()
    internal.name = employee.name
    internal.surname = employee.surname
    internal.patronymic = employee.patronymic
    internal.passport = employee.passport
    internal.phone = employee.phone
    internal.role = employee.role
    internal.city = employee.city
    internal.employment_date = get_datetime(employee.employment_date)
    internal.dismissal_date = get_datetime(employee.dismissal_date)
    internal.salary = employee.salary
    internal.shifts_history = list(map(get_datetime, employee.shifts_history))
    internal.vacation_history = list(map(from_vacation_dto, employee.vacation_history))
    internal.salary_change_history = list(map(from_salary_change_dto, employee.salary_change_history))
    return internal


def from_insert_branch_dto(branch: InsertBranchDto) -> InsertBranch:
    internal = InsertBranch()
    internal.name = branch.name
    internal.city = branch.city
    return internal


def from_query_dto(query: BranchQueryDto) -> BranchQuery:
    internal = BranchQuery()

    if query.name:
        internal.name = FieldEqualsValueQueryRepresentation(query.name[0], 'name')

    if query.city:
        internal.city = FieldEqualsValueQueryRepresentation(query.city[0], 'city')

    if query.id:
        internal.id = IdQueryRepresentation(ObjectId(query.id[0]))

    if not len(vars(internal)):
        raise EmptyQuery()

    return internal


def from_product_descriptor_dto(dto: ProductDescriptorDto) -> ProductDescriptor:
    internal = ProductDescriptor()
    internal.name = dto.name
    return internal


def from_insert_supplier_dto(supplier: InsertSupplierDto) -> InsertSupplier:
    internal = InsertSupplier()
    internal.name = supplier.name
    internal.phone = supplier.phone
    internal.email = supplier.email
    return internal


def from_insert_product_with_descriptor_dto(dto: InsertProductWithDescriptorDto) -> InsertProductWithDescriptor:
    internal = InsertProductWithDescriptor()
    internal.price = dto.price
    internal.descriptor = from_product_descriptor_dto(dto.descriptor)
    return internal


def from_employee_in_branch_query_dto(query: EmployeeInBranchQueryDto) -> EmployeeInBranchQuery:
    internal = EmployeeInBranchQuery()

    if query.name:
        internal.name = FieldEqualsValueQueryRepresentation(query.name[0], "employees.name")

    if query.patronymic:
        internal.patronymic = FieldEqualsValueQueryRepresentation(query.patronymic[0], "employees.patronymic")

    if query.surname:
        internal.surname = FieldEqualsValueQueryRepresentation(query.surname[0], "employees.surname")

    if query.role:
        internal.role = FieldEqualsValueQueryRepresentation(query.role[0], "employees.role")

    if query.phone_number:
        internal.phone_number = FieldEqualsValueQueryRepresentation(query.phone_number[0], "employees.phone_number")

    if query.id:
        internal.id = IdQueryRepresentation(ObjectId(query.id[0]), "employees._id")

    if query.salary_from or query.salary_to:
        salary_from = first(query.salary_from).map(float).or_else(None)
        salary_to = first(query.salary_to).map(float).or_else(None)
        internal.salary = IntervalQueryRepresentation(IntervalHolder(salary_from, salary_to),
                                                      "employees.salary")

    if query.dismissal_date_from or query.dismissal_date_to:
        date_from = first(query.dismissal_date_from).map(get_datetime).or_else(None)
        date_to = first(query.dismissal_date_to).map(get_datetime).or_else(None)
        internal.dismissal_date = IntervalQueryRepresentation(IntervalHolder(date_from, date_to),
                                                              "employees.dismissal_date")

    if query.employment_date_from or query.employment_date_to:
        date_from = first(query.employment_date_from).map(get_datetime).or_else(None)
        date_to = first(query.employment_date_to).map(get_datetime).or_else(None)
        internal.dismissal_date = IntervalQueryRepresentation(IntervalHolder(date_from, date_to),
                                                              "employees.employment_date")

    if not len(vars(internal)):
        raise EmptyQuery()

    return internal
