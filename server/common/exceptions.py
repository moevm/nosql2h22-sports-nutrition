from bson import ObjectId
from sanic.exceptions import InvalidUsage, NotFound


class ProjectException(Exception):
    pass


class NotFoundException(ProjectException):
    pass


class FileNotFoundException(NotFoundException):
    pass


class BadRequestException(InvalidUsage):
    pass


class InvalidObjectId(BadRequestException):
    def __init__(self, object_id: str):
        super().__init__(f"Failed to construct ObjectId from '{object_id}'")


class EmployeeNotFound(NotFound):
    def __init__(self, employee_id: ObjectId):
        super().__init__(f"Employee with id {employee_id} not found")
