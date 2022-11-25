from server.data.entity_to_service_mapper import from_branch_entity, from_supplier_entity_to_indexed
from server.data.service_to_entity_mapper import bson_from_branch, bson_from_supplier
from server.data.services.common.page import Page
from server.repository.maintenance_repository import MaintenanceRepository


class MaintenanceService:
    maintenance_repository: MaintenanceRepository

    def __init__(self, maintenance_repository: MaintenanceRepository):
        self.maintenance_repository = maintenance_repository

    async def get_branch_page(self, page: Page):
        return [from_branch_entity(entity) for entity in await self.maintenance_repository.page_branches(page)]

    async def insert_suppliers(self, suppliers: list) -> list:
        return await self.maintenance_repository.insert_suppliers(list(map(bson_from_supplier, suppliers)))

    async def insert_branches(self, branches: list) -> list:
        return await self.maintenance_repository.insert_branches(list(map(bson_from_branch, branches)))

    async def get_supplier_page(self, page: Page):
        return [from_supplier_entity_to_indexed(entity) for entity in
                await self.maintenance_repository.page_suppliers(page)]
