from datetime import datetime

from bson import ObjectId

from server.data.database.employee_entity import SalaryChangeEntity, VacationEntity, EmployeeEntity
from server.data.services.employee import SalaryChange, Vacation


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
    salary: int
    shifts_history: list
    vacation_history: list
    salary_change_history: list


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
