from bson import ObjectId

from server.common.logger import is_logged
from server.data.entity_mapper import entity_from_employee, entity_from_supplier
from server.data.services.branch.branch import Employee
from server.data.services.supplier.supplier import InsertSupplier
from server.repository.employees_repository import EmployeesRepository
from server.repository.supplier_repository import SupplierRepository


class EmployeesAccessor:
    repository: EmployeesRepository
    branch_id: ObjectId

    def __init__(self, repository: EmployeesRepository, branch_id: ObjectId):
        self.repository = repository
        self.branch_id = branch_id

    @is_logged(['class', 'request'])
    async def insert(self, request: Employee) -> ObjectId:
        return (await self.repository.insert(self.branch_id, entity_from_employee(request))).id


class SupplierService:
    #employees_repository: EmployeesRepository
    supplier_repository: SupplierRepository

    def __init__(self, supplier_repository: SupplierRepository):
        self.supplier_repository = supplier_repository

    # @is_logged(['class', 'branch_name'])
    # def employees(self, branch_id: ObjectId) -> EmployeesAccessor:
    #     return EmployeesAccessor(self.employees_repository, branch_id)

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertSupplier) -> ObjectId:
        return await self.supplier_repository.insert(entity_from_supplier(request))

    # @is_logged(['class', 'query'])
    # async def find_branches(self, query: BranchQuery) -> list:
    #     return [from_branch_entity(entity) for entity in await self.branch_repository.find_by_query(query)]
    #
    # @is_logged(['class', 'employee_id'])
    # async def find_employee_by_id(self, employee_id: ObjectId) -> EmployeeIndexed:
    #     return (await self.employees_repository.find_by_id(employee_id)) \
    #         .map(from_employee_entity) \
    #         .or_raise(lambda: EmployeeNotFound(employee_id))
