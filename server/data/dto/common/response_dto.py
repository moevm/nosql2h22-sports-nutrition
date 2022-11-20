from pydantic import BaseModel

from server.data.dto.common.page_dto import PageDto
from server.data.dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_employee_indexed


class FindListResponseDto(BaseModel):
    size: int
    result: list


class PageResponseDto(BaseModel):
    page: int
    size: int
    total: int
    items: list


def response_find_page(page: PageDto, response: list) -> PageResponseDto:
    result = PageResponseDto.construct()
    result.page = page.page
    result.size = page.size
    result.total = len(response)
    result.items = response
    return result


def response_find_employees(employees: list) -> FindListResponseDto:
    response = FindListResponseDto.construct()
    response.size = len(employees)
    response.result = list(dto_indexed_from_employee_indexed(employee).dict(by_alias=True) for employee in employees)
    return response


def response_find_branch(branches: list) -> FindListResponseDto:
    response = FindListResponseDto.construct()
    response.size = len(branches)
    response.result = list(dto_indexed_from_branch_indexed(branch).dict(by_alias=True) for branch in branches)
    return response
