from logging import info

from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.branch_entity import BranchEntity, from_branch_document, StockEntity, from_stock_document, \
    from_branch_info_document
from server.data.database.query import BranchQuery, StockInBranchQuery, IdQueryRepresentation
from server.data.dto.common.util import first
from server.data.services.common.page import Page
from server.database.mongo_connection import MongoConnection


class BranchRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_branches()

    @is_logged(['class', 'branch_id', 'stock'])
    async def add_stock(self, branch_id: ObjectId, stock: StockEntity) -> StockEntity:
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

    @is_logged(['class', 'page'])
    async def page(self, page: Page) -> list:
        return [from_branch_info_document(document) async for document in
                self.collection.find({}, {"name": 1, "city": 1}).skip(page.calculate_page()).limit(page.size)]

    @is_logged(['class', 'entity'])
    async def insert(self, request: BranchEntity) -> BranchEntity:
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request

    @is_logged(['class'])
    async def find_by_query(self, request: BranchQuery) -> list:
        query = request.get_json()
        info(f"query: {query}")
        return [from_branch_document(document) for document in
                await self.collection.find({"$and": query}).to_list(length=None)]

    @is_logged(['class', 'id'])
    async def find_by_id(self, branch_id: ObjectId) -> Optional:
        query = BranchQuery()
        query.id = IdQueryRepresentation(branch_id)
        return first(await self.find_by_query(query))

    @is_logged(['class', 'branch_id'])
    async def find_stock(self, branch_id: ObjectId, request: StockInBranchQuery) -> list:
        query = request.get_json()
        info(f"query: {query}")
        return [from_stock_document(document['stock']) for document in await self.collection.aggregate(
            [
                {
                    "$match": {
                        "_id": branch_id
                    }
                },
                {
                    "$unwind": "$stocks"
                },
                {
                    "$match": {
                        "$and": query
                    }
                },
                {
                    "$project": {
                        "stock": "$stocks"
                    }
                }
            ]).to_list(length=None)]
