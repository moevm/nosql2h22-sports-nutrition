from logging import info

from server.common.exceptions import SupplierNotFound
from server.data.database.branch_entity import ProductEntity
from server.database.mongo_connection import MongoConnection


class ProductRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()

    async def insert_with_description(self, product_entity: ProductEntity) -> ProductEntity:
        info(f"insert product_entity: {product_entity}")

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
