import configparser

from server.common.config import ProjectConfig, check_and_get_config_path
from server.common.mongo_config import ProjectConfigMongo
from server.common.web_config import ProjectConfigWeb
from server.database.mongo_connection import MongoConnection
from server.repository.employees_repository import EmployeesRepository
from server.service.employees_service import EmployeesService
from server.web.web_server import WebServer, InnerServerFactory

raw_config = configparser.ConfigParser()
raw_config.read(check_and_get_config_path())

config = ProjectConfig(raw_config)

mongo_config = ProjectConfigMongo(config)

web_config = ProjectConfigWeb(config)

web_server = WebServer(web_config, InnerServerFactory())

mongo_connection = MongoConnection(mongo_config)

employees_repository = EmployeesRepository(mongo_connection)

employees_service = EmployeesService(employees_repository)
