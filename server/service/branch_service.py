from bson import ObjectId

from server.common.exceptions import ProductNotFound, ProductAlreadyExists, BranchNotFound
from server.common.logger import is_logged
from server.data.database.query import product_id_query, Query
from server.data.dto_to_service_mapper import first
from server.data.entity_to_service_mapper import from_employee_entity, from_stock_entity, from_branch_entity, \
    from_branch_entity_to_info
from server.data.service_to_entity_mapper import entity_from_employee, entity_from_insert_branch, \
    entity_stock_from_product
from server.data.services.branch.branch import Employee, AddProduct, InsertBranch
from server.data.services.branch.branch_indexed import EmployeeIndexed, StockIndexed, BranchIndexed
from server.data.services.common.page import Page
from server.repository.branch_repository import BranchRepository
from server.repository.employees_repository import EmployeeRepository
from server.repository.product_repository import ProductRepository


class EmployeesAccessor:
    repository: EmployeeRepository
    branch_id: ObjectId

    def __init__(self, repository: EmployeeRepository, branch_id: ObjectId):
        self.repository = repository
        self.branch_id = branch_id

    @is_logged(['class', 'request'])
    async def insert(self, request: Employee) -> EmployeeIndexed:
        return from_employee_entity(await self.repository.insert(self.branch_id, entity_from_employee(request)))

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_employee_entity(entity) for entity in
                await self.repository.find_in_branch(self.branch_id, request)]


class StocksAccessor:
    branch_repository: BranchRepository
    product_repository: ProductRepository
    branch_id: ObjectId

    def __init__(self, branch_id: ObjectId, branch_repository: BranchRepository, product_repository: ProductRepository):
        self.branch_repository = branch_repository
        self.branch_id = branch_id
        self.product_repository = product_repository

    @is_logged(['class', 'request'])
    async def add(self, request: AddProduct) -> StockIndexed:
        await self.check_stock_not_present(request.product_id)

        product = (await self.product_repository.find_by_id(request.product_id)) \
            .or_raise(lambda: ProductNotFound(request.product_id))
        stock = entity_stock_from_product(product, request.price, request.amount)

        return from_stock_entity(await self.branch_repository.add_stock(self.branch_id, stock))

    @is_logged(['class', 'request'])
    async def find(self, request: Query) -> list:
        return [from_stock_entity(entity) for entity in
                await self.branch_repository.find_stock(self.branch_id, request)]

    @is_logged(['class', 'product_id'])
    async def check_stock_not_present(self, product_id: ObjectId):
        first(await self.find(product_id_query(product_id))) \
            .raise_if_present(lambda: ProductAlreadyExists(product_id, self.branch_id))


class BranchService:
    employees_repository: EmployeeRepository
    branch_repository: BranchRepository
    product_repository: ProductRepository

    def __init__(self,
                 employees_repository: EmployeeRepository,
                 branch_repository: BranchRepository,
                 product_repository: ProductRepository):
        self.employees_repository = employees_repository
        self.branch_repository = branch_repository
        self.product_repository = product_repository

    @is_logged(['class', 'branch_name'])
    async def employees(self, branch_id: ObjectId) -> EmployeesAccessor:
        return await self.access(branch_id, lambda: EmployeesAccessor(self.employees_repository, branch_id))

    @is_logged(['class', 'page'])
    async def page(self, page: Page):
        return [from_branch_entity_to_info(entity) for entity in await self.branch_repository.page(page)]

    @is_logged(['class', 'branch_id'])
    async def stocks(self, branch_id: ObjectId) -> StocksAccessor:
        return await self.access(branch_id,
                                 lambda: StocksAccessor(branch_id, self.branch_repository, self.product_repository))

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertBranch) -> BranchIndexed:
        return from_branch_entity(await self.branch_repository.insert(entity_from_insert_branch(request)))

    @is_logged(['class', 'query'])
    async def find_branches(self, query: Query) -> list:
        return [from_branch_entity(entity) for entity in await self.branch_repository.find_by_query(query)]

    @is_logged(['class', 'request'])
    async def find_employee(self, request: Query) -> list:
        return [from_employee_entity(entity) for entity in await self.employees_repository.find(request)]

    async def access(self, branch_id: ObjectId, accessor_function):
        (await self.branch_repository.find_by_id(branch_id)).or_raise(lambda: BranchNotFound(branch_id))
        return accessor_function()
