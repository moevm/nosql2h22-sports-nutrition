from bson import ObjectId
from dataclasses import dataclass
from datetime import datetime
from pydantic import Field

from server.data.database.common import PydanticObjectId

@dataclass
class InsertSale:
    supplier_id: PydanticObjectId
    product_id: PydanticObjectId
    branch_id: PydanticObjectId
    price: float
    amount: int
    date: datetime

@dataclass
class SaleIndexed:
    id: ObjectId
    supplier_id: PydanticObjectId
    product_id: PydanticObjectId
    branch_id: PydanticObjectId
    price: float
    amount: int
    date: datetime
