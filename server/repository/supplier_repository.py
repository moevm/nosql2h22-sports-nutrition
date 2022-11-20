from logging import info

from bson import ObjectId

from server.common.monad import Optional
from server.data.database.supplier_entity import SupplierEntity, from_supplier_document
from server.database.mongo_connection import MongoConnection


class SupplierRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()

    async def insert(self, request: SupplierEntity) -> SupplierEntity:
        info(f"insert supplier {request}")
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        info(f"inserted: {request}")
        return request

    async def find_by_id(self, object_id: ObjectId) -> Optional:
        info(f"find by id: {object_id}")
        return Optional(await self.collection.find_one({"_id": object_id})).map(from_supplier_document)