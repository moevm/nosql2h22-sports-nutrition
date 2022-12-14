from bson import ObjectId

from server.common.exceptions import SupplierNotFound
from server.common.logger import is_logged
from server.data.database.query import Query
from server.data.entity_to_service_mapper import from_product_entity, from_supplier_entity_to_info, \
    from_supplier_entity_to_indexed
from server.data.service_to_entity_mapper import entity_from_supplier, entity_from_insert_product_with_descriptor
from server.data.services.branch.branch_indexed import ProductIndexed
from server.data.services.common.page import Page
from server.data.services.product.product import InsertProductWithDescriptor
from server.data.services.supplier.supplier import InsertSupplier, SupplierIndexed
from server.repository.product_repository import ProductRepository
from server.repository.supplier_repository import SupplierRepository


class ProductsAccessor:
    repository: ProductRepository
    supplier_id: ObjectId

    def __init__(self, repository: ProductRepository, supplier_id: ObjectId):
        self.repository = repository
        self.supplier_id = supplier_id

    @is_logged(['class', 'request'])
    async def insert_with_descriptor(self, request: InsertProductWithDescriptor) -> ProductIndexed:
        repository_request = entity_from_insert_product_with_descriptor(self.supplier_id, request)
        return from_product_entity(await self.repository.insert_with_description(repository_request))

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_product_entity(entity) for entity in
                await self.repository.find_by_query_in_supplier(self.supplier_id, request)]


class SupplierService:
    supplier_repository: SupplierRepository
    product_repository: ProductRepository

    def __init__(self, supplier_repository: SupplierRepository, product_repository: ProductRepository):
        self.supplier_repository = supplier_repository
        self.product_repository = product_repository

    @is_logged(['class', 'supplier_id'])
    async def products(self, supplier_id: ObjectId) -> ProductsAccessor:
        return await self.access(supplier_id, lambda: ProductsAccessor(self.product_repository, supplier_id))

    @is_logged(['class', 'page'])
    async def page(self, page: Page) -> list:
        return [from_supplier_entity_to_info(entity) for entity in await self.supplier_repository.page(page)]

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertSupplier) -> SupplierIndexed:
        return from_supplier_entity_to_indexed(await self.supplier_repository.insert(entity_from_supplier(request)))

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_supplier_entity_to_indexed(entity) for entity in await self.supplier_repository.find(request)]

    async def access(self, supplier_id: ObjectId, accessor_function):
        (await self.supplier_repository.find_by_id(supplier_id)).or_raise(lambda: SupplierNotFound(supplier_id))
        return accessor_function()
