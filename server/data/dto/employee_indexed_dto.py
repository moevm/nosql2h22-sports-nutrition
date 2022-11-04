from typing import List

from pydantic import BaseModel

from server.data.dto.employee_dto import VacationDto, SalaryChangeDto


class EmployeeIndexedDto(BaseModel):
    id: str
    name: str
    surname: str
    patronymic: str
    passport: str
    phone: str
    role: str
    city: str
    employment_date: str
    dismissal_date: str
    salary: int
    shifts_history: List[str]
    vacation_history: List[VacationDto]
    salary_change_history: List[SalaryChangeDto]
