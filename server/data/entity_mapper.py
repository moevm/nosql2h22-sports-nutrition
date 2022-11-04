from server.data.database.employee_entity import EmployeeEntity, SalaryChangeEntity, VacationEntity
from server.data.services.employee import Employee, Vacation, SalaryChange


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