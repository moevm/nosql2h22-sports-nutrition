from datetime import datetime

from bson import ObjectId

from server.common.exceptions import InvalidBranchQuery
from server.data.datetime_formatter import get_datetime
from server.data.dto.branch_dto import InsertEmployeeDto, SalaryChangeDto, VacationDto, InsertBranchDto, BranchQueryDto, \
    DtoConstant


class BranchQuery:
    name: str
    city: str
    _id: ObjectId

    def __repr__(self) -> str:
        return str(vars(self))


class SalaryChange:
    salary_before: int
    salary_after: int
    date: datetime


class Vacation:
    payments: int
    start_date: datetime
    end_date: datetime


class Employee:
    name: str
    surname: str
    patronymic: str
    passport: str
    phone: str
    role: str
    city: str
    employment_date: datetime
    dismissal_date: datetime
    salary: int
    shifts_history: list
    vacation_history: list
    salary_change_history: list


class InsertBranch:
    name: str
    city: str


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

    if hasattr(query, "name") and query.name and len(query.name) < DtoConstant.STRING_SIZE:
        internal.name = query.name[0]

    if hasattr(query, "city") and query.city and len(query.city) < DtoConstant.STRING_SIZE:
        internal.city = query.city[0]

    if hasattr(query, "id") and query.id:
        internal._id = ObjectId(query.id[0])

    if not len(vars(internal)):
        raise InvalidBranchQuery()

    return internal
