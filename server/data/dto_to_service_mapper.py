from bson import ObjectId

from server.common.exceptions import EmptyQuery
from server.common.monad import Optional
from server.data.database.query import BranchQuery, FieldEqualsValueQueryRepresentation, IdQueryRepresentation, \
    EmployeeInBranchQuery, IntervalQueryRepresentation, IntervalHolder, StockInBranchQuery
from server.data.datetime_formatter import get_datetime
from server.data.dto.branch.branch_dto import AddProductDto, SalaryChangeDto, VacationDto, InsertEmployeeDto, \
    InsertBranchDto, BranchQueryDto, EmployeeInBranchQueryDto, StockInBranchQueryDto
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
    return AddProduct(ObjectId(request.product_id), request.price, request.amount)


def from_salary_change_dto(change: SalaryChangeDto) -> SalaryChange:
    return SalaryChange(change.salary_before, change.salary_after, get_datetime(change.date))


def from_vacation_dto(vacation: VacationDto) -> Vacation:
    return Vacation(vacation.payments, get_datetime(vacation.start_date), get_datetime(vacation.end_date))


def from_employee_dto(employee: InsertEmployeeDto) -> Employee:
    return Employee(employee.name, employee.surname, employee.patronymic, employee.passport, employee.phone,
                    employee.role, employee.city, get_datetime(employee.employment_date),
                    get_datetime(employee.dismissal_date), employee.salary,
                    list(map(get_datetime, employee.shifts_history)),
                    list(map(from_vacation_dto, employee.vacation_history)),
                    list(map(from_salary_change_dto, employee.salary_change_history)))


def from_insert_branch_dto(branch: InsertBranchDto) -> InsertBranch:
    return InsertBranch(branch.name, branch.city)


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
    return ProductDescriptor(dto.name)


def from_insert_supplier_dto(supplier: InsertSupplierDto) -> InsertSupplier:
    return InsertSupplier(supplier.name, supplier.phone, supplier.email)


def from_insert_product_with_descriptor_dto(dto: InsertProductWithDescriptorDto) -> InsertProductWithDescriptor:
    return InsertProductWithDescriptor(dto.price, from_product_descriptor_dto(dto.descriptor))


def from_stock_in_branch_query_dto(query: StockInBranchQueryDto) -> StockInBranchQuery:
    internal = StockInBranchQuery()

    if query.name:
        internal.name = FieldEqualsValueQueryRepresentation(query.name[0], "stocks.product.descriptor.name")

    if query.id:
        internal.id = IdQueryRepresentation(ObjectId(query.id[0]), "stocks._id")

    if query.supplier_id:
        internal.supplier_id = FieldEqualsValueQueryRepresentation(ObjectId(query.supplier_id[0]),
                                                                   "stocks.product.supplier_id")

    if query.product_id:
        internal.product_id = FieldEqualsValueQueryRepresentation(ObjectId(query.product_id[0]),
                                                                  "stocks.product._id")

    if query.amount_from or query.amount_to:
        amount_from = first(query.amount_from).map(int).or_else(None)
        amount_to = first(query.amount_to).map(int).or_else(None)
        internal.amount = IntervalQueryRepresentation(IntervalHolder(amount_from, amount_to),
                                                      "stocks.amount")

    if query.price_from or query.price_to:
        price_from = first(query.price_from).map(int).or_else(None)
        price_to = first(query.price_to).map(int).or_else(None)
        internal.amount = IntervalQueryRepresentation(IntervalHolder(price_from, price_to),
                                                      "stocks.price")
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
