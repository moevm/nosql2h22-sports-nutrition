from server.database.mongo_connection import MongoConnection
from server.common.logger import is_logged
from server.data.database.sale_entity import SaleEntity
from server.data.database.query import Query
from server.data.database.sale_entity import from_sale_document
from logging import info
from server.repository.branch_repository import BranchRepository
from bson import ObjectId
from server.data.datetime_formatter import get_string

class SaleRepository:
    def __init__(self, connection: MongoConnection, branch_repository: BranchRepository):
        self.collection = connection.get_sales()
        self.branch_repository = branch_repository

    @is_logged(['class', 'entity'])
    async def insert(self, request: SaleEntity) -> SaleEntity:
        # print(f"request.id info: {type(request.id)}")
        
        # ищем нужный брэнч
        branch = (await self.branch_repository.find_by_id(ObjectId(request.branch_id))).get()
        # ищем stock с request.product_id
        stock = None
        for branch_stock in branch.stocks:
            if branch_stock.product.id == request.product_id:
                stock = branch_stock
        # смотрим на его количество
        if stock.amount < request.amount:
            raise ValueError("too big amount for sale")

        # уменьшаем количество товара
        await self.branch_repository.update_stock_amount(stock.id, stock.amount - request.amount)

        request.id = (await self.collection.insert_one(request.dict(by_alias=True))).inserted_id
        return request
    
    @is_logged(['class'])
    async def find_by_query(self, request: Query) -> list:
        query = request.get_json()
        info(f"query: {query}")
        return [from_sale_document(document) for document in
                await self.collection.find(request.get_json()).to_list(length=None)]

    @is_logged(['class'])
    async def get_all_sales(self) -> list:
        cursor = self.collection.find({})
        all_sales = []
        # while cursor.has_next():
        #     all_sales.append(await cursor.next())

        while (await cursor.fetch_next):
            doc = cursor.next_object()
            doc["_id"] = str(doc["_id"])
            doc["product_id"] = str(doc["product_id"])
            doc["supplier_id"] = str(doc["supplier_id"])
            doc["branch_id"] = str(doc["branch_id"])
            doc["date"] = get_string(doc["date"])
            all_sales.append(doc)
    
        return all_sales
