from logging import info

from bson import ObjectId

from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.employee_entity import EmployeeEntity, from_employee_document
from server.database.mongo_connection import MongoConnection


class EmployeesRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_employees()

    @is_logged()
    async def insert(self, request: EmployeeEntity) -> ObjectId:
        info(f"insert employee: {request}")
        return await self.collection.insert_one(request.dict())

    @is_logged()
    async def find(self, employee_id: ObjectId) -> Optional:
        return Optional(from_employee_document(await self.collection.find_one({'_id': employee_id})))
