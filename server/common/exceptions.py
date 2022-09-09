class ProjectException(Exception):
    pass


class NotFoundException(ProjectException):
    pass


class FileNotFoundException(NotFoundException):
    pass
