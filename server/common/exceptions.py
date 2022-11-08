from bson import ObjectId
from sanic.exceptions import InvalidUsage, NotFound


class FileNotFound(NotFound):
    pass


class EmployeeNotFound(NotFound):
    def __init__(self, employee_id: ObjectId):
        super().__init__(f"Employee with id {employee_id} not found")


class BranchNotFound(NotFound):
    def __init__(self, branch_description):
        super().__init__(f"Branch with given description '{branch_description}' not found")


class InvalidBranchQuery(InvalidUsage):
    def __init__(self):
        super().__init__("Query must have at least one condition. Name and City must contain less than 30 symbols")


class InvalidSupplierQuery(InvalidUsage):
    def __init__(self):
        super().__init__("Query must have at least one condition: name, phone or email")
