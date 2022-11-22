from dataclasses import dataclass

from bson import ObjectId


@dataclass
class InsertSupplier:
    name: str
    email: str
    phone: str


@dataclass
class SupplierIndexed:
    id: ObjectId
    name: str
    email: str
    phone: str
    products: list
