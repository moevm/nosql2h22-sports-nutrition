from dataclasses import dataclass

from server.data.dto.common.page_dto import PageDto, SupplierPageDto


@dataclass
class Page:
    number: int
    size: int

    def calculate_page(self) -> int:
        return (self.number - 1) * self.size


@dataclass
class SupplierPage(Page):
    products_size: int


def from_page_dto(page: PageDto) -> Page:
    return Page(page.page, page.size)


def from_supplier_page_dto(page: SupplierPageDto) -> SupplierPage:
    return SupplierPage(page.page, page.size, page.products_size)
