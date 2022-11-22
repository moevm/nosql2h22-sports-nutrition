from logging import info

from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.data.database.branch_entity import BranchEntity, from_branch_document, StockEntity
from server.data.database.query import BranchQuery
from server.data.services.common.page import Page
from server.database.mongo_connection import MongoConnection


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

    async def page(self, page: Page) -> list:
        info(f"find page: {page.get_page()}, size: {page.size}")
        return [from_branch_document(document) async for document in
                self.collection.find({}).skip(page.get_page()).limit(page.size)]

    async def insert(self, request: BranchEntity) -> BranchEntity:
        info(f"insert branch {request}")
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        info(f"inserted: {request}")
        return request

    async def find_by_query(self, request: BranchQuery) -> list:
        query = request.get_json()
        info(f"query: {query}")
        return [from_branch_document(document) for document in
                await self.collection.find({"$and": query}).to_list(length=None)]
