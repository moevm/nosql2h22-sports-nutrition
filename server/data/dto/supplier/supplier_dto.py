from typing import Any

from pydantic import BaseModel, Field

from server.data.dto.branch.branch_dto import DtoConstant


class ProductInSupplierQueryDto(BaseModel):
    ids: Any = Field(None, alias="_id")
    names: Any = Field(None)
    descriptor_ids: Any = Field(None)
    price_from: Any = Field(None)
    price_to: Any = Field(None)


class ProductQueryDto(BaseModel):
    ids: Any = Field(None, alias="_id")
    names: Any = Field(None)
    descriptor_ids: Any = Field(None)
    price_from: Any = Field(None)
    price_to: Any = Field(None)
    supplier_ids: Any = Field(None)


class SupplierQueryDto(BaseModel):
    ids: Any = Field(None, alias="_id")
    name: Any = Field(None)
    phone: Any = Field(None)
    email: Any = Field(None)
    product_names: Any = Field(None)
    product_ids: Any = Field(None)
    descriptor_ids: Any = Field(None)


class InsertSupplierDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    phone: str = Field(..., regex=DtoConstant.PHONE_REGEX, max_length=DtoConstant.MAX_STRING_SIZE,
                       min_length=DtoConstant.MIN_STRING_SIZE)
    email: str = Field(..., regex=DtoConstant.EMAIL_REGEX, max_length=DtoConstant.MAX_STRING_SIZE,
                       min_length=DtoConstant.MIN_STRING_SIZE)
