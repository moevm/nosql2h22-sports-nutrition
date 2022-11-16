from server.data.dto.product.product_dto import InsertProductWithDescriptorDto, ProductDescriptorDto


class ProductDescriptor:
    name: str


class InsertProductWithDescriptor:
    price: float
    descriptor: ProductDescriptor


def from_product_descriptor_dto(dto: ProductDescriptorDto):
    internal = ProductDescriptor()
    internal.name = dto.name
    return internal


def from_insert_product_with_descriptor_dto(dto: InsertProductWithDescriptorDto):
    internal = InsertProductWithDescriptor()
    internal.price = dto.price
    internal.descriptor = from_product_descriptor_dto(dto.descriptor)
    return internal
