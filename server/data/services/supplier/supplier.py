from bson import ObjectId

from server.common.exceptions import InvalidSupplierQuery
from server.data.database.supplier_entity import SupplierEntity
from server.data.dto.branch.branch_dto import DtoConstant
from server.data.dto.supplier.supplier_dto import InsertSupplierDto, SupplierQueryDto
from server.data.services.branch.branch_indexed import from_product_entity


class SupplierQuery:
    name: str
    email: str
    phone: str
    _id: ObjectId

    def __repr__(self) -> str:
        return str(vars(self))


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


def from_supplier_query_dto(query: SupplierQueryDto) -> SupplierQuery:
    internal = SupplierQuery()

    if hasattr(query, "name") and query.name and len(query.name) < DtoConstant.MAX_STRING_SIZE:
        internal.name = query.name[0]

    if hasattr(query, "phone") and query.phone and len(query.phone) < DtoConstant.MAX_STRING_SIZE:
        internal.phone = query.phone[0]

    if hasattr(query, "email") and query.email and len(query.email) < DtoConstant.MAX_STRING_SIZE:
        internal.email = query.email[0]

    if hasattr(query, "id") and query.id:
        internal._id = ObjectId(query.id[0])

    if not len(vars(internal)):
        raise InvalidSupplierQuery()

    return internal


def from_supplier_entity_to_indexed(supplier: SupplierEntity):
    internal = SupplierIndexed()
    internal.name = supplier.name
    internal.phone = supplier.phone
    internal.id = supplier.id
    internal.email = supplier.email
    internal.products = list(map(from_product_entity, supplier.products))
    return internal
