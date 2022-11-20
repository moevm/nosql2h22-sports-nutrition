from pydantic import BaseModel, Field

from server.data.dto.branch.branch_dto import DtoConstant


class SupplierQueryDto(BaseModel):
    name: str = Field(max_length=DtoConstant.MAX_STRING_SIZE)
    phone: str = Field(max_length=DtoConstant.MAX_STRING_SIZE)
    email: str = Field(max_length=DtoConstant.MAX_STRING_SIZE)
    id: str = Field(alias="_id")


class InsertSupplierDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.MAX_STRING_SIZE, min_length=DtoConstant.MIN_STRING_SIZE)
    phone: str = Field(..., regex=DtoConstant.PHONE_REGEX, max_length=DtoConstant.MAX_STRING_SIZE,
                       min_length=DtoConstant.MIN_STRING_SIZE)
    email: str = Field(..., regex=DtoConstant.EMAIL_REGEX, max_length=DtoConstant.MAX_STRING_SIZE,
                       min_length=DtoConstant.MIN_STRING_SIZE)
