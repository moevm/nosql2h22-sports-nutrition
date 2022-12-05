from pydantic import BaseModel
from datetime import datetime

from server.data.database.common import PydanticObjectId


class SaleIndexedDto(BaseModel):
    id: str # = Field(alias='_id')
    supplier_id: PydanticObjectId
    product_id: PydanticObjectId
    branch_id: PydanticObjectId
    price: float
    amount: int
    date: str
