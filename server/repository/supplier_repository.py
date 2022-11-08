from logging import info

from bson import ObjectId

from server.data.database.supplier_entity import SupplierEntity
from server.database.mongo_connection import MongoConnection


class SupplierRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()

    async def insert(self, request: SupplierEntity) -> ObjectId:
        info(f"insert supplier {request}")
        return (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id

