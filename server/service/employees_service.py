import json

from bson import ObjectId

from server.common.logger import is_logged
from server.repository.employees_repository import EmployeesRepository


class EmployeesService:

    def __init__(self, repository: EmployeesRepository):
        self.repository = repository

    @is_logged()
    async def insert(self, request: json):
        return await self.repository.insert(request)

    @is_logged()
    async def find(self, employee_id: str) -> json:
        result = await self.repository.find(ObjectId(employee_id))
        return {
            "name": result['name']
        }
