from sanic.exceptions import InvalidUsage


class ProjectException(Exception):
    pass


class NotFoundException(ProjectException):
    pass


class FileNotFoundException(NotFoundException):
    pass


class BadRequestException(InvalidUsage):
    pass


class InvalidObjectId(BadRequestException):
    def __init__(self, id: str):
        super().__init__(f"Failed to construct ObjectId from '{id}'")
