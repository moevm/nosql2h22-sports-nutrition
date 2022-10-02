import json

from bson import ObjectId

from server.common.logger import is_logged
from server.database.mongo_connection import MongoConnection


class EmployeesRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_employees()

    @is_logged()
    async def insert(self, request: json):
        return await self.collection.insert_one(request)

    @is_logged()
    async def find(self, employee_id: ObjectId):
        return await self.collection.find_one({'_id': employee_id})
