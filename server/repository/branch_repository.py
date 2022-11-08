from logging import info

from bson import ObjectId

from server.data.database.branch_entity import BranchEntity, from_branch_document
from server.data.services.branch.branch import BranchQuery
from server.database.mongo_connection import MongoConnection
from server.repository.query_parser import parse_query_items


class BranchRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_branches()

    async def insert(self, request: BranchEntity) -> ObjectId:
        info(f"insert branch {request}")
        return (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id

    async def find_by_query(self, query: BranchQuery) -> list:
        parsed = parse_query_items(vars(query).items())
        info(f"query: {parsed}")
        return [from_branch_document(document) for document in
                await self.collection.find({"$and": parsed}).to_list(length=100)]
