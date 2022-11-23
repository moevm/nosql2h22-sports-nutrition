from server.data.entity_to_service_mapper import from_branch_entity, from_supplier_entity_to_indexed
from server.data.services.common.page import Page
from server.repository.maintenance_repository import MaintenanceRepository


class MaintenanceService:
    maintenance_repository: MaintenanceRepository

    def __init__(self, maintenance_repository: MaintenanceRepository):
        self.maintenance_repository = maintenance_repository

    async def branch_page(self, page: Page):
        return [from_branch_entity(entity) for entity in await self.maintenance_repository.page_branches(page)]

    async def supplier_page(self, page: Page):
        return [from_supplier_entity_to_indexed(entity) for entity in
                await self.maintenance_repository.page_suppliers(page)]
