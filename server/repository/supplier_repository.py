from dataclasses import dataclass

from bson import ObjectId

from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.query import QueryBuilder, Query
from server.data.database.supplier_entity import SupplierEntity, from_supplier_document, from_supplier_info_document
from server.data.dto.common.util import first
from server.data.services.common.page import SupplierPage
from server.database.mongo_connection import MongoConnection


@dataclass
class Token:
    PRODUCTS: str = "$products"


class SupplierRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()

    @is_logged(['class', 'entity'])
    async def insert(self, request: SupplierEntity) -> SupplierEntity:
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request

    @is_logged(['class', 'page'])
    async def page(self, page: SupplierPage) -> list:
        return [from_supplier_info_document(document) for document in await self.collection.aggregate([
            {
                "$project": {
                    "name": 1,
                    "email": 1,
                    "phone": 1,
                    "products": {
                        "$map": {
                            "input": {
                                "$slice": ["$products", page.products_size]
                            },
                            "as": "product",
                            "in": "$$product.descriptor.name"
                        }
                    }
                },
            },
            {
                "$skip": page.calculate_page()
            },
            {
                "$limit": page.size
            }]).to_list(length=None)]

    @is_logged(['class', 'supplier_id'])
    async def find_by_id(self, supplier_id: ObjectId) -> Optional:
        return first(await self.find(QueryBuilder().and_condition().field("_id").equals(supplier_id).compile()))

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_supplier_document(document) for document in
                await self.collection.find(request.get_json()).to_list(length=None)]
