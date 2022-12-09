from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.common.logger import is_logged
from server.data.database.branch_entity import EmployeeEntity, from_employee_document
from server.data.database.query import Query
from server.database.mongo_connection import MongoConnection


class EmployeeRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_branches()

    @is_logged(['class', 'branch_id', 'entity'])
    async def insert(self, branch_id: ObjectId, request: EmployeeEntity) -> EmployeeEntity:
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

    @is_logged(['class', 'branch_id'])
    async def find_in_branch(self, branch_id: ObjectId, request: Query) -> list:
        return [from_employee_document(document['employee']) for document in await self.collection.aggregate(
            [
                {
                    "$match": {
                        "_id": branch_id
                    }
                },
                {
                    "$unwind": "$employees"
                },
                {
                    "$match": request.get_json()
                },
                {
                    "$project": {
                        "employee": "$employees"
                    }
                }
            ]).to_list(length=None)]

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_employee_document(document['employee']) for document in await self.collection.aggregate(
            [
                {
                    "$unwind": "$employees"
                },
                {
                    "$match": request.get_json()
                },
                {
                    "$project": {
                        "employee": "$employees"
                    }
                }
            ]).to_list(length=None)]
