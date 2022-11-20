from bson import ObjectId

from server.common.exceptions import EmployeeNotFound, ProductNotFound
from server.common.logger import is_logged
from server.data.entity_mapper import entity_from_employee, entity_from_branch, entity_stock_from_product
from server.data.services.branch.branch import Employee, InsertBranch, BranchQuery, AddProduct
from server.data.services.branch.branch_indexed import EmployeeIndexed, from_employee_entity, from_branch_entity, \
    StockIndexed, from_stock_entity, BranchIndexed
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
        product = (await self.product_repository.find_by_id(request.product_id)) \
            .or_raise(lambda: ProductNotFound(request.product_id))
        stock = entity_stock_from_product(product, request.price, request.amount)
        return from_stock_entity(await self.branch_repository.add_stock(self.branch_id, stock))


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
    def employees(self, branch_id: ObjectId) -> EmployeesAccessor:
        return EmployeesAccessor(self.employees_repository, branch_id)

    @is_logged(['class', 'branch_id'])
    def stocks(self, branch_id: ObjectId) -> StocksAccessor:
        return StocksAccessor(branch_id, self.branch_repository, self.product_repository)

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertBranch) -> BranchIndexed:
        return from_branch_entity(await self.branch_repository.insert(entity_from_branch(request)))

    @is_logged(['class', 'query'])
    async def find_branches(self, query: BranchQuery) -> list:
        return [from_branch_entity(entity) for entity in await self.branch_repository.find_by_query(query)]

    @is_logged(['class', 'employee_id'])
    async def find_employee_by_id(self, employee_id: ObjectId) -> EmployeeIndexed:
        return (await self.employees_repository.find_by_id(employee_id)) \
            .map(from_employee_entity) \
            .or_raise(lambda: EmployeeNotFound(employee_id))
