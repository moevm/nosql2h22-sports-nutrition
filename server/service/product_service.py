from server.common.logger import is_logged
from server.data.database.query import Query
from server.data.entity_to_service_mapper import from_product_entity
from server.repository.product_repository import ProductRepository


class ProductService:
    product_repository: ProductRepository

    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_product_entity(entity) for entity in await self.product_repository.find_by_query(request)]
