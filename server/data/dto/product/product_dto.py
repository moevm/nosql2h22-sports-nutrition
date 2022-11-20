from pydantic import BaseModel, Field

from server.data.dto.common.constant import DtoConstant


class ProductDescriptorDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)


class InsertProductWithDescriptorDto(BaseModel):
    price: float = Field(..., gt=0)
    descriptor: ProductDescriptorDto = Field(...)
