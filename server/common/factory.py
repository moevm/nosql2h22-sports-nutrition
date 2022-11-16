import configparser

from server.common.config import ProjectConfig, check_and_get_config_path
from server.common.mongo_config import ProjectConfigMongo
from server.common.web_config import ProjectConfigWeb
from server.database.mongo_connection import MongoConnection
from server.repository.branch_repository import BranchRepository
from server.repository.employees_repository import EmployeeRepository
from server.repository.product_repository import ProductRepository
from server.repository.supplier_repository import SupplierRepository
from server.service.branch_service import BranchService
from server.service.supplier_service import SupplierService
from server.web.web_server import WebServer, InnerServerFactory

raw_config = configparser.ConfigParser()
raw_config.read(check_and_get_config_path())

config = ProjectConfig(raw_config)

mongo_config = ProjectConfigMongo(config)

web_config = ProjectConfigWeb(config)

web_server = WebServer(web_config, InnerServerFactory())

mongo_connection = MongoConnection(mongo_config)

employee_repository = EmployeeRepository(mongo_connection)

branch_repository = BranchRepository(mongo_connection)

branch_service = BranchService(employee_repository, branch_repository)

supplier_repository = SupplierRepository(mongo_connection)

product_repository = ProductRepository(mongo_connection)

supplier_service = SupplierService(supplier_repository, product_repository)
