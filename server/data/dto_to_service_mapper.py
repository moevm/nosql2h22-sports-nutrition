from bson import ObjectId

from server.common.exceptions import InvalidPhoneQuery
from server.common.monad import Optional
from server.data.database.query import Query, IntervalHolder
from server.data.database.query import QueryBuilder
from server.data.database.query import regex
from server.data.datetime_formatter import get_datetime
from server.data.dto.branch.branch_dto import AddStockDto, SalaryChangeDto, VacationDto, InsertEmployeeDto, \
    InsertBranchDto, BranchQueryDto, EmployeeQueryDto, StockQueryDto
from server.data.dto.branch.branch_indexed_dto import IndexedBranchesDto, BranchDto, StockIndexedDto, \
    ProductIndexedDto, ProductDescriptorIndexedDto, EmployeeIndexedDto
from server.data.dto.common.util import unpack_first, split_query_string, object_id, first
from server.data.dto.product.product_dto import ProductDescriptorDto, InsertProductWithDescriptorDto
from server.data.dto.supplier.supplier_dto import InsertSupplierDto, SupplierQueryDto, ProductQueryDto
from server.data.dto.supplier.supplier_indexed_dto import SupplierDto
from server.data.services.branch.branch import AddProduct, SalaryChange, Vacation, Employee, InsertBranch
from server.data.services.branch.branch_indexed import StockIndexed, ProductIndexed, \
    ProductDescriptorIndexed, EmployeeIndexed, Branch
from server.data.services.product.product import ProductDescriptor, InsertProductWithDescriptor
from server.data.services.supplier.supplier import InsertSupplier, Supplier


def from_product_descriptor_indexed_dto(request: ProductDescriptorIndexedDto) -> ProductDescriptorIndexed:
    return ProductDescriptorIndexed(ObjectId(request.id), request.name)


def from_product_indexed_dto(request: ProductIndexedDto) -> ProductIndexed:
    return ProductIndexed(ObjectId(request.id), from_product_descriptor_indexed_dto(request.descriptor),
                          ObjectId(request.supplier_id), request.price)


def from_stock_indexed_dto(request: StockIndexedDto) -> StockIndexed:
    return StockIndexed(ObjectId(request.id), request.amount, request.price, from_product_indexed_dto(request.product))


def from_branch_dto(request: BranchDto) -> Branch:
    return Branch(request.name, request.city,
                  list(map(from_stock_indexed_dto, request.stocks)),
                  list(map(from_employee_indexed_dto, request.employees)))


def from_supplier_dto(request: SupplierDto) -> Supplier:
    return Supplier(request.name, request.email, request.phone, list(map(from_product_indexed_dto, request.products)))


def from_branches_indexed_dto(request: IndexedBranchesDto) -> list:
    return list(map(from_branch_dto, request.branches))


def from_add_product_dto(request: AddStockDto) -> AddProduct:
    return AddProduct(ObjectId(request.product_id), request.price, request.amount)


def from_salary_change_dto(change: SalaryChangeDto) -> SalaryChange:
    return SalaryChange(change.salary_before, change.salary_after, get_datetime(change.date))


def from_vacation_dto(vacation: VacationDto) -> Vacation:
    return Vacation(vacation.payments, get_datetime(vacation.start_date), get_datetime(vacation.end_date))


def from_employee_indexed_dto(employee: EmployeeIndexedDto) -> EmployeeIndexed:
    return EmployeeIndexed(ObjectId(employee.id), employee.name, employee.surname, employee.patronymic,
                           employee.passport, employee.phone,
                           employee.role, employee.city, get_datetime(employee.employment_date),
                           get_datetime(employee.dismissal_date), employee.salary,
                           list(map(get_datetime, employee.shifts_history)),
                           list(map(from_vacation_dto, employee.vacation_history)),
                           list(map(from_salary_change_dto, employee.salary_change_history)))


def from_employee_dto(employee: InsertEmployeeDto) -> Employee:
    return Employee(employee.name, employee.surname, employee.patronymic, employee.passport, employee.phone,
                    employee.role, employee.city, get_datetime(employee.employment_date),
                    Optional(employee.dismissal_date).map(get_datetime).or_else(None), employee.salary,
                    list(map(get_datetime, employee.shifts_history)),
                    list(map(from_vacation_dto, employee.vacation_history)),
                    list(map(from_salary_change_dto, employee.salary_change_history)))


def from_insert_branch_dto(branch: InsertBranchDto) -> InsertBranch:
    return InsertBranch(branch.name, branch.city)


def get_interval_holder(value_from: list, value_to: list, mapper):
    value = None

    if value_from or value_to:
        value = IntervalHolder(first(value_from).map(mapper).or_else(None),
                               first(value_to).map(mapper).or_else(None))

    return value


def from_branch_query_dto(query: BranchQueryDto) -> Query:
    return QueryBuilder() \
        .and_condition().field("name").equals_regex(unpack_first(query.name)) \
        .and_condition().field("city").equals_regex(unpack_first(query.city)) \
        .and_condition().field("_id").equals(object_id(query.id)) \
        .and_condition().field("stocks.product.descriptor.name").contains_all(split_query_string(query.product_names)) \
        .and_condition().field("stocks.product._id").contains_all(query_ids(query.product_ids)) \
        .and_condition().field("employees._id").contains_all(query_ids(query.employee_ids)) \
        .and_condition().field("employees.name").contains_all(split_query_string(query.employee_names)) \
        .and_condition().field("employees.surname").contains_all(split_query_string(query.employee_surnames)) \
        .and_condition().field("stocks").size_in_interval(get_interval_holder(query.stocks_from,
                                                                              query.stocks_to,
                                                                              int)) \
        .and_condition().field("employees").size_in_interval(get_interval_holder(query.employees_from,
                                                                                 query.employees_to,
                                                                                 int)) \
        .compile()


def query_phone(phone_query: list) -> str:
    if phone_query is None:
        return None

    phone = unpack_first(phone_query)

    if not phone.isnumeric():
        raise InvalidPhoneQuery(phone)

    return phone


def query_ids(query: list) -> list:
    return map_query_list(query, ObjectId)


def map_query_list(query: list, mapper) -> list:
    if query is None:
        return None

    return [mapper(query_element) for query_element in split_query_string(query)]


def from_supplier_query_dto(query: SupplierQueryDto) -> Query:
    return QueryBuilder() \
        .and_condition().field("name").equals_regex(unpack_first(query.name)) \
        .and_condition().field("email").equals_regex(unpack_first(query.email)) \
        .and_condition().field("phone").equals_regex(query_phone(query.phone)) \
        .and_condition().field("products.descriptor.name").contains_all(map_query_list(query.product_names, regex)) \
        .and_condition().field("products.descriptor._id").contains_all(query_ids(query.descriptor_ids)) \
        .and_condition().field("products._id").contains_all(query_ids(query.product_ids)) \
        .and_condition().field("_id").in_list(query_ids(query.ids)) \
        .compile()


def from_product_query_dto(query: ProductQueryDto) -> Query:
    return QueryBuilder() \
        .and_condition().field("products._id").in_list(query_ids(query.ids)) \
        .and_condition().field("products.supplier_id").contains_all(query_ids(query.supplier_ids)) \
        .and_condition().field("products.descriptor._id").contains_all(query_ids(query.descriptor_ids)) \
        .and_condition().field("products.descriptor.name").contains_all(map_query_list(query.names, regex)) \
        .and_condition().field("products.price").in_interval(get_interval_holder(query.price_from,
                                                                                 query.price_to,
                                                                                 float)) \
        .compile()


def from_product_descriptor_dto(dto: ProductDescriptorDto) -> ProductDescriptor:
    return ProductDescriptor(dto.name)


def from_insert_supplier_dto(supplier: InsertSupplierDto) -> InsertSupplier:
    return InsertSupplier(supplier.name, supplier.phone, supplier.email)


def from_insert_product_with_descriptor_dto(dto: InsertProductWithDescriptorDto) -> InsertProductWithDescriptor:
    return InsertProductWithDescriptor(dto.price, from_product_descriptor_dto(dto.descriptor))


def from_stock_in_branch_query_dto(query: StockQueryDto) -> Query:
    return QueryBuilder() \
        .and_condition().field("stocks.product.descriptor.name").equals_regex(unpack_first(query.name)) \
        .and_condition().field("stocks._id").in_list(query_ids(query.ids)) \
        .and_condition().field("stocks.product.supplier_id").equals(object_id(query.supplier_id)) \
        .and_condition().field("stocks.product._id").equals(object_id(query.product_id)) \
        .and_condition().field("stocks.amount").in_interval(get_interval_holder(query.amount_from,
                                                                                query.amount_to,
                                                                                int)) \
        .and_condition().field("stocks.price").in_interval(get_interval_holder(query.price_from,
                                                                               query.price_to,
                                                                               float)) \
        .compile()


def from_employee_query_dto(query: EmployeeQueryDto) -> Query:
    return QueryBuilder() \
        .and_condition().field("employees.name").equals_regex(unpack_first(query.name)) \
        .and_condition().field("employees.patronymic").equals_regex(unpack_first(query.patronymic)) \
        .and_condition().field("employees.surname").equals_regex(unpack_first(query.surname)) \
        .and_condition().field("employees.role").equals_regex(unpack_first(query.role)) \
        .and_condition().field("employees.phone").equals_regex(query_phone(query.phone_number)) \
        .and_condition().field("employees._id").equals(object_id(query.id)) \
        .and_condition().field("employees.salary").in_interval(get_interval_holder(query.salary_from,
                                                                                   query.salary_to,
                                                                                   float)) \
        .and_condition().field("employees.dismissal_date").in_interval(get_interval_holder(query.dismissal_date_from,
                                                                                           query.dismissal_date_to,
                                                                                           get_datetime)) \
        .and_condition().field("employees.employment_date").in_interval(get_interval_holder(query.employment_date_from,
                                                                                            query.employment_date_to,
                                                                                            get_datetime)) \
        .compile()
