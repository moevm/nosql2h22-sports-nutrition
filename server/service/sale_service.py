from server.repository.sale_repository import SaleRepository


class SaleService:
    sale_repository: SaleRepository

    def __init__(self,
                 sale_repository: SaleRepository):
        self.sale_repository = sale_repository
