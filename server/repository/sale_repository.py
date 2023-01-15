from server.database.mongo_connection import MongoConnection
from server.common.logger import is_logged
from server.data.database.sale_entity import SaleEntity
from server.data.database.query import Query
from server.data.database.sale_entity import from_sale_document
from logging import info
from server.repository.branch_repository import BranchRepository
from bson import ObjectId

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
