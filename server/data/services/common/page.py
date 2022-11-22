from dataclasses import dataclass

from server.data.dto.common.page_dto import PageDto


@dataclass
class Page:
    number: int
    size: int

    def get_page(self) -> int:
        return self.number - 1


def from_page_dto(page: PageDto) -> Page:
    return Page(page.page, page.size)
