from server.common.logger import is_logged
from server.data.database.branch_entity import from_branch_document
from server.data.database.supplier_entity import from_supplier_document
from server.data.services.common.page import Page
from server.database.mongo_connection import MongoConnection


class MaintenanceRepository:

    def __init__(self, connection: MongoConnection):
        self.branches = connection.get_branches()
        self.suppliers = connection.get_suppliers()

    @is_logged(['class', 'page'])
    async def page_branches(self, page: Page) -> list:
        return [from_branch_document(document) async for document in
                self.branches.find().skip(page.calculate_page()).limit(page.size)]

    @is_logged(['class', 'page'])
    async def page_suppliers(self, page: Page) -> list:
        return [from_supplier_document(document) async for document in
                self.suppliers.find().skip(page.calculate_page()).limit(page.size)]

    @is_logged(['class', 'suppliers'])
    async def insert_suppliers(self, suppliers: list) -> list:
        return (await self.suppliers.insert_many(suppliers)).inserted_ids

    @is_logged(['class', 'branches'])
    async def insert_branches(self, branches: list) -> list:
        return (await self.branches.insert_many(branches)).inserted_ids
