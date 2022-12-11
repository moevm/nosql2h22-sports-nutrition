from dataclasses import dataclass

from bson import ObjectId

from server.common.exceptions import BranchNotFound
from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.branch_entity import BranchEntity, from_branch_document, StockEntity, from_stock_document, \
    from_branch_info_document
from server.data.database.query import QueryBuilder, Query
from server.data.dto.common.util import first
from server.data.services.common.page import Page
from server.database.mongo_connection import MongoConnection


@dataclass
class Token:
    EMPLOYEES: str = "$employees"
    STOCKS: str = "$stocks"


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
        return [from_branch_info_document(document) for document in await self.collection.aggregate([
            {
                "$project": {
                    "name": 1,
                    "city": 1,
                    "employees": {
                        "$cond": {
                            "if": {
                                "$isArray": Token.EMPLOYEES
                            },
                            "then": {
                                "$size": Token.EMPLOYEES
                            },
                            "else": "-1"
                        }
                    },
                    "stocks": {
                        "$cond": {
                            "if": {
                                "$isArray": Token.STOCKS
                            },
                            "then": {
                                "$size": Token.STOCKS
                            },
                            "else": "-1"
                        }
                    }
                }
            },
            {
                "$skip": page.calculate_page()
            },
            {
                "$limit": page.size
            }
        ]).to_list(length=None)]

    @is_logged(['class', 'entity'])
    async def insert(self, request: BranchEntity) -> BranchEntity:
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request

    @is_logged(['class', 'request'])
    async def find_by_query(self, request: Query) -> list:
        return [from_branch_document(document) for document in
                await self.collection.find(request.get_json()).to_list(length=None)]

    @is_logged(['class', 'id'])
    async def find_by_id(self, branch_id: ObjectId) -> Optional:
        return first(await self.find_by_query(QueryBuilder().and_condition().field("_id").equals(branch_id).compile()))

    @is_logged(['class', 'branch_id', 'request'])
    async def find_stock(self, branch_id: ObjectId, request: Query) -> list:
        return [from_stock_document(document['stock']) for document in await self.collection.aggregate(
            [
                {
                    "$match": {
                        "_id": branch_id
                    }
                },
                {
                    "$unwind": Token.STOCKS
                },
                {
                    "$match": request.get_json()
                },
                {
                    "$project": {
                        "stock": Token.STOCKS
                    }
                }
            ]).to_list(length=None)]
