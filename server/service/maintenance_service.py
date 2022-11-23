from server.repository.branch_repository import BranchRepository
from server.repository.supplier_repository import SupplierRepository


class MaintenanceService:
    branch_repository: BranchRepository
    supplier_repository: SupplierRepository

    def __init__(self, branch_repository: BranchRepository, supplier_repository: SupplierRepository):
        self.branch_repository = branch_repository
        self.supplier_repository = supplier_repository
