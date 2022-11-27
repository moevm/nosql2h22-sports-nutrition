from dataclasses import dataclass

from bson import ObjectId


@dataclass
class InsertSupplier:
    name: str
    email: str
    phone: str


@dataclass
class Supplier:
    name: str
    email: str
    phone: str
    products: list


@dataclass
class SupplierIndexed:
    id: ObjectId
    name: str
    email: str
    phone: str
    products: list


@dataclass
class SupplierInfo:
    id: ObjectId
    name: str
    email: str
    phone: str
    products: int
