from server.database.mongo_connection import MongoConnection

class SaleRepository:
    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_sales()
