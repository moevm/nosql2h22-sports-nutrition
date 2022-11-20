from logging import info

from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.data.database.branch_entity import BranchEntity, from_branch_document, StockEntity
from server.data.services.branch.branch import BranchQuery
from server.database.mongo_connection import MongoConnection
from server.repository.query_parser import parse_query_items


class BranchRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_branches()

    async def add_stock(self, branch_id: ObjectId, stock: StockEntity) -> StockEntity:
        info(f"add_stock to branch {branch_id}: {stock}")

        updated = (await self.collection.update_one(
            {
                "_id": branch_id
            },
            {
                "$push": {
                    "stocks": stock.dict(by_alias=True)
                }
            })).modified_count

        if not updated:
            raise BranchNotFound(branch_id)

        return stock

    async def insert(self, request: BranchEntity) -> BranchEntity:
        info(f"insert branch {request}")
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        info(f"inserted: {request}")
        return request

    async def find_by_query(self, query: BranchQuery) -> list:
        parsed = parse_query_items(vars(query).items())
        info(f"query: {parsed}")
        return [from_branch_document(document) for document in
                await self.collection.find({"$and": parsed}).to_list(length=100)]
