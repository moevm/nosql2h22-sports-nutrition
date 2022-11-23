from pydantic import BaseModel

from server.data.dto.common.page_dto import PageDto
from server.data.service_to_dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_employee_indexed, \
    dto_indexed_from_stock_indexed, dto_indexed_from_supplier


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


def response_find_stocks(stocks: list) -> FindListResponseDto:
    response = FindListResponseDto.construct()
    response.size = len(stocks)
    response.result = list(dto_indexed_from_stock_indexed(stock).dict(by_alias=True) for stock in stocks)
    return response


def response_find_list(data: list, mapper) -> FindListResponseDto:
    response = FindListResponseDto.construct()
    response.size = len(data)
    response.result = list(mapper(element).dict(by_alias=True) for element in data)
    return response


def response_find_branch(branches: list) -> FindListResponseDto:
    return response_find_list(branches, dto_indexed_from_branch_indexed)


def response_find_supplier(suppliers: list) -> FindListResponseDto:
    return response_find_list(suppliers, dto_indexed_from_supplier)
