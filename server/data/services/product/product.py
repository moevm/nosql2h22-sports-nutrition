from dataclasses import dataclass


@dataclass
class ProductDescriptor:
    name: str


@dataclass
class InsertProductWithDescriptor:
    price: float
    descriptor: ProductDescriptor
