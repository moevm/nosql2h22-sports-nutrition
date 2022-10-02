from dataclasses import dataclass

from server.common.config import ProjectConfig


@dataclass
class WebConfigConstant:
    MONGO_CONFIG_TOKEN: str = "Mongo"
    URL_TOKEN: str = "url"
    DATABASE_TOKEN: str = "database"


class ProjectConfigMongo(ProjectConfig):

    def __init__(self, configuration: ProjectConfig):
        super().__init__(configuration.get_config()[WebConfigConstant.MONGO_CONFIG_TOKEN])

    def get_config(self):
        return super().get_config()

    def get_url(self):
        return self.get_config()[WebConfigConstant.URL_TOKEN]

    def get_database(self):
        return self.get_config()[WebConfigConstant.DATABASE_TOKEN]
