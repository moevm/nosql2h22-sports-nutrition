from bson import ObjectId

from server.common.logger import is_logged
from server.common.monad import Optional
from server.data.database.supplier_entity import SupplierEntity, from_supplier_document
from server.data.services.common.page import Page
from server.database.mongo_connection import MongoConnection


class SupplierRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()

    @is_logged(['class', 'entity'])
    async def insert(self, request: SupplierEntity) -> SupplierEntity:
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request

    @is_logged(['class', 'page'])
    async def page(self, page: Page) -> list:
        return [from_supplier_document(document) async for document in
                self.collection.find({}).skip(page.get_page()).limit(page.size)]

    @is_logged(['class', 'supplier_id'])
    async def find_by_id(self, supplier_id: ObjectId) -> Optional:
        return Optional(await self.collection.find_one({"_id": supplier_id})).map(from_supplier_document)
