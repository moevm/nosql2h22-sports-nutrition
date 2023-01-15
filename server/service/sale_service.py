from server.repository.sale_repository import SaleRepository


class SaleService:
    sale_repository: SaleRepository

    def __init__(self,
                 sale_repository: SaleRepository):
        self.sale_repository = sale_repository

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertSale) -> SaleIndexed:
        return from_sale_entity(await self.sale_repository.insert(entity_from_insert_sale(request)))
