from bson import ObjectId

from server.common.logger import is_logged
from server.data.entity_mapper import entity_from_employee, entity_from_supplier
from server.data.services.branch.branch import Employee
from server.data.services.supplier.supplier import InsertSupplier
from server.repository.employees_repository import EmployeesRepository
from server.repository.product_repository import ProductsRepository
from server.repository.supplier_repository import SupplierRepository


class ProductsAccessor:
    repository: ProductsRepository
    supplier_id: ObjectId

    def __init__(self, repository: ProductsRepository, supplier_id: ObjectId):
        self.repository = repository
        self. supplier_id = supplier_id


class SupplierService:
    supplier_repository: SupplierRepository

    def __init__(self, supplier_repository: SupplierRepository):
        self.supplier_repository = supplier_repository

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertSupplier) -> ObjectId:
        return await self.supplier_repository.insert(entity_from_supplier(request))

