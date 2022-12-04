from typing import Any
from pydantic import BaseModel, Field
from datetime import datetime

from server.data.database.common import PydanticObjectId


class SaleQueryDto(BaseModel):
    supplier_id: Any = Field(None)
    product_id: Any = Field(None)
    branch_id: Any = Field(None)
    id: Any = Field(None, alias="_id")

class InsertSaleDto(BaseModel):
    supplier_id: Any = Field(None)
    product_id: Any = Field(None)
    branch_id: Any = Field(None)
    price: float = Field(..., ge=0)
    amount: int = Field(..., ge=0)
    # timestamp: datetime = Field(None)
