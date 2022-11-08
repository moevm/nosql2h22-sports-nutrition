from bson import ObjectId

from server.common.exceptions import SupplierNotFound
from server.common.logger import is_logged
from server.data.entity_mapper import entity_from_supplier
from server.data.services.supplier.supplier import InsertSupplier, SupplierIndexed, from_supplier_entity_to_indexed
from server.repository.product_repository import ProductsRepository
from server.repository.supplier_repository import SupplierRepository


class ProductsAccessor:
    repository: ProductsRepository
    supplier_id: ObjectId

    def __init__(self, repository: ProductsRepository, supplier_id: ObjectId):
        self.repository = repository
        self.supplier_id = supplier_id


class SupplierService:
    supplier_repository: SupplierRepository

    def __init__(self, supplier_repository: SupplierRepository):
        self.supplier_repository = supplier_repository

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertSupplier) -> ObjectId:
        return await self.supplier_repository.insert(entity_from_supplier(request))

    @is_logged(['class', 'object_id'])
    async def find_by_id(self, object_id: ObjectId) -> SupplierIndexed:
        return (await self.supplier_repository.find_by_id(object_id)) \
            .map(from_supplier_entity_to_indexed) \
            .or_raise(lambda: SupplierNotFound(object_id))
