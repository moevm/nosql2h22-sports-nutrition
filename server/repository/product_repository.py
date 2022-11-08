from server.database.mongo_connection import MongoConnection


class ProductsRepository:

    def __init__(self, connection: MongoConnection):
        self.collection = connection.get_suppliers()