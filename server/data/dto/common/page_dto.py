from pydantic import BaseModel, validator
from sanic.exceptions import InvalidUsage


def validate_number(number: list, argument_name: str) -> int:
    number = number[0]

    if type(number) is not str or not number.isdigit():
        raise InvalidUsage(f'{argument_name} must be a number')

    number = int(number)

    if number <= 0:
        raise InvalidUsage(f'{argument_name} must be a positive value')

    return number


class PageDto(BaseModel):
    page: list
    size: list

    @validator('page')
    def positive_page(cls, page):
        return validate_number(page, 'page')

    @validator('size')
    def positive_size(cls, size):
        return validate_number(size, 'size')
