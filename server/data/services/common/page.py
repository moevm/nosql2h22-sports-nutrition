from server.data.dto.common.page_dto import PageDto


class Page:
    number: int
    size: int

    def get_page(self) -> int:
        return self.number - 1


def from_page_dto(page: PageDto) -> Page:
    internal = Page()
    internal.number = page.page
    internal.size = page.size
    return internal
