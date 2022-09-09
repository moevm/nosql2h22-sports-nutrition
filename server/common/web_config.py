from dataclasses import dataclass
from enum import Enum

from server.common.config import ProjectConfig, config


@dataclass
class WebConfigConstant:
    WEB_CONFIG_TOKEN: str = "Web"
    HOST_TOKEN: str = "host"
    PORT_TOKEN: str = "port"
    SERVER_TYPE_TOKEN: str = "server_type"


class ServerType(Enum):
    Sanic = 1


class ProjectConfigWeb(ProjectConfig):

    def __init__(self, configuration: ProjectConfig):
        super().__init__(configuration.get_config()[WebConfigConstant.WEB_CONFIG_TOKEN])

    def get_config(self):
        return super().get_config()

    def get_host(self) -> str:
        return self.get_config()[WebConfigConstant.HOST_TOKEN]

    def get_port(self) -> int:
        return int(self.get_config()[WebConfigConstant.PORT_TOKEN])

    def get_server_type(self) -> ServerType:
        return ServerType[self.get_config()[WebConfigConstant.SERVER_TYPE_TOKEN]]


web_config = ProjectConfigWeb(config)
