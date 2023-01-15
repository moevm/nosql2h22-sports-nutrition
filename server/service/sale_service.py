from server.repository.sale_repository import SaleRepository
from server.common.logger import is_logged
from server.data.services.sale.sale import InsertSale
from server.data.services.sale.sale import SaleIndexed
from server.data.service_to_entity_mapper import entity_from_insert_sale
from server.data.entity_to_service_mapper import from_sale_entity
from server.data.database.query import Query

class SaleService:
    sale_repository: SaleRepository

    def __init__(self,
                 sale_repository: SaleRepository):
        self.sale_repository = sale_repository

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertSale) -> SaleIndexed:
        return from_sale_entity(await self.sale_repository.insert(entity_from_insert_sale(request)))
    
    @is_logged(['class', 'query'])
    async def find_sales(self, query: Query) -> list:
        return [from_sale_entity(entity) for entity in await self.sale_repository.find_by_query(query)]
