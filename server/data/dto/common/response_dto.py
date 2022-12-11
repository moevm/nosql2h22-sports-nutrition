from bson import ObjectId
from pydantic import BaseModel

from server.data.database.common import SerializableObjectId
from server.data.dto.common.page_dto import PageDto
from server.data.service_to_dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_employee_indexed, \
    dto_indexed_from_stock_indexed, dto_indexed_from_supplier, dto_indexed_from_product_indexed


class ListResponseDto(BaseModel):
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


def response_find_employees(employees: list) -> ListResponseDto:
    return response_find_list(employees, dto_indexed_from_employee_indexed)


def response_find_stocks(stocks: list) -> ListResponseDto:
    return response_find_list(stocks, dto_indexed_from_stock_indexed)


def response_insert_ids(object_ids: list) -> ListResponseDto:
    return response_find_list(object_ids, to_serializable_object_id)


def to_serializable_object_id(object_id: ObjectId) -> SerializableObjectId:
    response = SerializableObjectId.construct()
    response.id = str(object_id)
    return response


def response_find_list(data: list, mapper) -> ListResponseDto:
    response = ListResponseDto.construct()
    response.size = len(data)
    response.result = list(mapper(element).dict(by_alias=True) for element in data)
    return response


def response_find_branch(branches: list) -> ListResponseDto:
    return response_find_list(branches, dto_indexed_from_branch_indexed)


def response_find_supplier(suppliers: list) -> ListResponseDto:
    return response_find_list(suppliers, dto_indexed_from_supplier)


def response_find_product(products: list) -> ListResponseDto:
    return response_find_list(products, dto_indexed_from_product_indexed)
