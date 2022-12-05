from typing import List

from pydantic import Field, BaseModel

from server.data.dto.branch.branch_indexed_dto import ProductIndexedDto


class SupplierIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    email: str
    phone: str
    products: List[ProductIndexedDto] = []


class SupplierDto(BaseModel):
    name: str
    email: str
    phone: str
    products: List[ProductIndexedDto] = []


class SuppliersDto(BaseModel):
    suppliers: List[SupplierDto]


class SupplierInfoDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    email: str
    phone: str
    products: int
