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


class ProductNotFound(NotFound):
    def __init__(self, product_id):
        super().__init__(f"Product with id {product_id} not found")


class SupplierNotFound(NotFound):
    def __init__(self, supplier_id):
        super().__init__(f"Supplier with id '{supplier_id}' not found")


class ProductAlreadyExists(InvalidUsage):
    def __init__(self, product_id, branch_id):
        super().__init__(f"Product with id '{product_id}' alredy present in branch '{branch_id}'")


class EmptyQuery(InvalidUsage):
    def __init__(self):
        super().__init__("Query must have at least one condition")
