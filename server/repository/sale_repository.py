from server.database.mongo_connection import MongoConnection

class SaleRepository:
    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_sales()

    @is_logged(['class', 'entity'])
    async def insert(self, request: SaleEntity) -> SaleEntity:
        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request
