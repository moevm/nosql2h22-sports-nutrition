from logging import info
from typing import List

from pydantic import BaseModel, Field

from server.data.database.branch_entity import ProductEntity, from_product_document
from server.data.database.common import PydanticObjectId


class SupplierEntity(BaseModel):
    id: PydanticObjectId = Field(alias='_id')
    name: str
    email: str
    phone: str
    products: List[ProductEntity] = []


def from_supplier_document(document) -> SupplierEntity:
    info(f"parse document: {document}")

    entity = SupplierEntity.construct()
    entity.id = document['_id']
    entity.name = document['name']
    entity.email = document['email']
    entity.phone = document['phone']
    entity.products = list(map(from_product_document, document['products']))
    return entity


def from_supplier_info_document(document) -> SupplierEntity:
    info(f"parse document: {document}")

    entity = SupplierEntity.construct()
    entity.id = document['_id']
    entity.name = document['name']
    return entity
