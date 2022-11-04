from bson import ObjectId

from server.common.exceptions import EmployeeNotFound
from server.common.logger import is_logged
from server.data.entity_mapper import entity_from_employee
from server.data.services.employee import Employee
from server.data.services.employee_indexed import from_employee_entity, EmployeeIndexed
from server.repository.employees_repository import EmployeesRepository


class EmployeesService:

    def __init__(self, repository: EmployeesRepository):
        self.repository = repository

    @is_logged()
    async def insert(self, request: Employee) -> ObjectId:
        return await self.repository.insert(entity_from_employee(request))

    @is_logged()
    async def find(self, employee_id: ObjectId) -> EmployeeIndexed:
        return from_employee_entity((await self.repository.find(employee_id))
                                    .or_raise(lambda: EmployeeNotFound(employee_id)))
