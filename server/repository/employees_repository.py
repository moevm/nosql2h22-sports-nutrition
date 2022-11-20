from logging import info

from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.common.monad import Optional
from server.data.database.branch_entity import EmployeeEntity, from_employee_document
from server.database.mongo_connection import MongoConnection


class EmployeeRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_branches()

    async def insert(self, branch_id: ObjectId, request: EmployeeEntity) -> EmployeeEntity:
        info(f"insert to {branch_id} employee: {request}")

        updated = (await self.collection.update_one(
            {
                "_id": branch_id
            },
            {
                "$push": {
                    "employees": request.dict(by_alias=True)
                }
            })).modified_count

        if not updated:
            raise BranchNotFound(branch_id)

        return request

    async def find_by_id(self, employee_id: ObjectId) -> Optional:
        info(f"find_by_id: {employee_id}")
        return Optional(await self.collection.find_one(
            {
                "employees._id": employee_id
            },
            {
                "employees.$": 1
            })).map(lambda branch: branch['employees'][0]).map(from_employee_document)
