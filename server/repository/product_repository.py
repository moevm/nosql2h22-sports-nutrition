from dataclasses import dataclass

from bson import ObjectId

from server.common.exceptions import SupplierNotFound
from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.branch_entity import ProductEntity, from_product_document
from server.data.database.query import Query
from server.database.mongo_connection import MongoConnection


@dataclass
class Constant:
    PRODUCTS: str = "$products"


class ProductRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()

    @is_logged(['class', 'entity'])
    async def insert_with_description(self, product_entity: ProductEntity) -> ProductEntity:
        updated = (await self.collection.update_one(
            {
                "_id": product_entity.supplier_id
            },
            {
                "$push": {
                    "products": product_entity.dict(by_alias=True)
                }
            })).modified_count

        if not updated:
            raise SupplierNotFound(product_entity.supplier_id)

        return product_entity

    @is_logged(['class', 'product_id'])
    async def find_by_id(self, product_id: ObjectId) -> Optional:
        return Optional(await self.collection.find_one(
            {
                "products._id": product_id
            },
            {
                "products.$": 1
            })).map(lambda supplier: supplier['products'][0]).map(from_product_document)

    @is_logged(['class', 'query'])
    async def find_by_query(self, request: Query) -> list:
        return [from_product_document(document['product']) for document in await self.collection.aggregate(
            [
                {
                    "$unwind": Constant.PRODUCTS
                },
                {
                    "$match": request.get_json()
                },
                {
                    "$project": {
                        "product": Constant.PRODUCTS
                    }
                }
            ]).to_list(length=None)]

    @is_logged(['class', 'supplier_id', 'query'])
    async def find_by_query_in_supplier(self, supplier_id: ObjectId, request: Query) -> list:
        return [from_product_document(document['product']) for document in await self.collection.aggregate(
            [
                {
                    "$match": {
                        "_id": supplier_id
                    }
                },
                {
                    "$unwind": Constant.PRODUCTS
                },
                {
                    "$match": request.get_json()
                },
                {
                    "$project": {
                        "product": Constant.PRODUCTS
                    }
                }
            ]).to_list(length=None)]
