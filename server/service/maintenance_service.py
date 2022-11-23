from server.data.entity_to_service_mapper import from_branch_entity, from_supplier_entity_to_indexed
from server.repository.branch_repository import BranchRepository
from server.repository.supplier_repository import SupplierRepository


class MaintenanceService:
    branch_repository: BranchRepository
    supplier_repository: SupplierRepository

    def __init__(self, branch_repository: BranchRepository, supplier_repository: SupplierRepository):
        self.branch_repository = branch_repository
        self.supplier_repository = supplier_repository

    async def get_branches(self) -> list:
        return [from_branch_entity(entity) for entity in await self.branch_repository.find_all()]

    async def get_suppliers(self) -> list:
        return [from_supplier_entity_to_indexed(entity) for entity in await self.supplier_repository.find_all()]
