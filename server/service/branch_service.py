from bson import ObjectId

from server.common.exceptions import EmployeeNotFound
from server.common.logger import is_logged
from server.data.entity_mapper import entity_from_employee, entity_from_branch
from server.data.services.branch import Employee, InsertBranch, BranchQuery
from server.data.services.branch_indexed import EmployeeIndexed, from_employee_entity, from_branch_entity
from server.repository.branch_repository import BranchRepository
from server.repository.employees_repository import EmployeesRepository


class EmployeesAccessor:
    repository: EmployeesRepository
    branch_id: ObjectId

    def __init__(self, repository: EmployeesRepository, branch_id: ObjectId):
        self.repository = repository
        self.branch_id = branch_id

    @is_logged(['class', 'request'])
    async def insert(self, request: Employee) -> ObjectId:
        return (await self.repository.insert(self.branch_id, entity_from_employee(request))).id


class BranchService:
    employees_repository: EmployeesRepository
    branch_repository: BranchRepository

    def __init__(self, employees_repository: EmployeesRepository, branch_repository: BranchRepository):
        self.employees_repository = employees_repository
        self.branch_repository = branch_repository

    @is_logged(['class', 'branch_name'])
    def employees(self, branch_id: ObjectId) -> EmployeesAccessor:
        return EmployeesAccessor(self.employees_repository, branch_id)

    @is_logged(['class', 'request'])
    async def insert(self, request: InsertBranch) -> ObjectId:
        return await self.branch_repository.insert(entity_from_branch(request))

    @is_logged(['class', 'query'])
    async def find_branches(self, query: BranchQuery) -> list:
        return [from_branch_entity(entity) for entity in await self.branch_repository.find_by_query(query)]

    @is_logged(['class', 'employee_id'])
    async def find_employee_by_id(self, employee_id: ObjectId) -> EmployeeIndexed:
        return (await self.employees_repository.find_by_id(employee_id)) \
            .map(from_employee_entity) \
            .or_raise(lambda: EmployeeNotFound(employee_id))
