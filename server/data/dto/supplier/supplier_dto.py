from typing import Optional, Any

from pydantic import BaseModel, Field

from server.data.dto.branch.branch_dto import DtoConstant


class SupplierQueryDto(BaseModel):
    name: Optional[Any] = None
    phone: Optional[Any] = None
    email: Optional[Any] = None
    id: Any = Field(None, alias="_id")


class InsertSupplierDto(BaseModel):
    name: str = Field(..., max_length=DtoConstant.STRING_SIZE)
    phone: str = Field(..., regex=r"^(\+)[1-9][0-9\-\(\)\.]{9,15}$")
    email: str = Field(..., regex=r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")


