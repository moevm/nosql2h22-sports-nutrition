from bson import ObjectId
from pydantic import BaseModel, Field


class BaseInsertResponseDto(BaseModel):
    id: str = Field(alias='_id')


class InsertEmployeeResponseDto(BaseInsertResponseDto):
    pass


class InsertBranchResponseDto(BaseInsertResponseDto):
    pass


class InsertSupplierResponseDto(BaseInsertResponseDto):
    pass


def insert_branch_response(object_id: ObjectId) -> InsertBranchResponseDto:
    response = InsertBranchResponseDto.construct()
    response.id = str(object_id)
    return response


def insert_employee_response(object_id: ObjectId) -> InsertEmployeeResponseDto:
    response = InsertEmployeeResponseDto.construct()
    response.id = str(object_id)
    return response


def insert_supplier_response(object_id: ObjectId) -> InsertSupplierResponseDto:
    response = InsertSupplierResponseDto.construct()
    response.id = str(object_id)
    return response
