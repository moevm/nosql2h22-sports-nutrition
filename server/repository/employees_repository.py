from logging import info

from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.branch_entity import EmployeeEntity, from_employee_document
from server.data.database.query import EmployeeInBranchQuery
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
    async def find_by_query(self, branch_id: ObjectId, request: EmployeeInBranchQuery) -> list:
        query = request.get_json()
        info(f"query: {query}")
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
                    "$match": {
                        "$and": query
                    }
                },
                {
                    "$project": {
                        "employee": "$employees"
                    }
                }
            ]).to_list(length=None)]

    @is_logged(['class', 'employee_id'])
    async def find_by_id(self, employee_id: ObjectId) -> Optional:
        return Optional(await self.collection.find_one(
            {
                "employees._id": employee_id
            },
            {
                "employees.$": 1
            })).map(lambda branch: branch['employees'][0]).map(from_employee_document)
