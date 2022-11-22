from bson import ObjectId


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
