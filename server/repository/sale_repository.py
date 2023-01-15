from server.database.mongo_connection import MongoConnection
from server.common.logger import is_logged
from server.data.database.sale_entity import SaleEntity
from server.data.database.query import Query
from server.data.database.sale_entity import from_sale_document
from logging import info

class SaleRepository:
    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_sales()

    @is_logged(['class', 'entity'])
    async def insert(self, request: SaleEntity) -> SaleEntity:
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request
    
    @is_logged(['class'])
    async def find_by_query(self, request: Query) -> list:
        query = request.get_json()
        info(f"query: {query}")
        return [from_sale_document(document) for document in
                await self.collection.find(request.get_json()).to_list(length=None)]
