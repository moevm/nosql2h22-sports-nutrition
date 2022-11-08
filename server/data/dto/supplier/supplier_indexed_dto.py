from pydantic import Field, BaseModel


class SupplierIndexedDto(BaseModel):
    id: str = Field(alias='_id')
    name: str
    email: str
    phone: str
    products: list

