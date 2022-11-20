from bson import ObjectId

from server.data.database.supplier_entity import SupplierEntity
from server.data.dto.supplier.supplier_dto import InsertSupplierDto
from server.data.services.branch.branch_indexed import from_product_entity


class InsertSupplier:
    name: str
    email: str
    phone: str


class SupplierIndexed:
    id: ObjectId
    name: str
    email: str
    phone: str
    products: list


def from_insert_supplier_dto(supplier: InsertSupplierDto) -> InsertSupplier:
    internal = InsertSupplier()
    internal.name = supplier.name
    internal.phone = supplier.phone
    internal.email = supplier.email
    return internal


def from_supplier_entity_to_indexed(supplier: SupplierEntity):
    internal = SupplierIndexed()
    internal.name = supplier.name
    internal.phone = supplier.phone
    internal.id = supplier.id
    internal.email = supplier.email
    internal.products = list(map(from_product_entity, supplier.products))
    return internal
