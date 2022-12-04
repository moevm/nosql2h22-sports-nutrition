from datetime import datetime

from pydantic import BaseModel, Field

from server.data.database.common import PydanticObjectId

from logging import info
from server.common.logger import is_logged

class SaleEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    supplier_id: PydanticObjectId
    product_id: PydanticObjectId
    branch_id: PydanticObjectId
    price: float
    amount: int
    # timestamp: datetime

def from_sale_document(document) -> SaleEntity:
    entity = SaleEntity.construct()
    entity.id = document['_id']
    entity.supplier_id = document['supplier_id']
    entity.product_id = document['product_id']
    entity.branch_id = document['branch_id']
    entity.price = document['price']
    entity.amount = document['amount']
    # entity.timestamp = document['timestamp']
    return entity
