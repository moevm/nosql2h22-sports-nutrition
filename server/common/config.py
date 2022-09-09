import configparser
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

from server.common.path_utils import check_path_exists


@dataclass
class ConfigConstant:
    CONFIG_FILE_NAME: str = 'config.ini'


def check_and_get_config_path():
    current_path = os.path.dirname(__file__)
    relative_path = f"../resources/{ConfigConstant.CONFIG_FILE_NAME}"
    return check_path_exists(os.path.join(current_path, relative_path))


class ProjectBaseConfig(ABC):
    @abstractmethod
    def get_config(self):
        pass


class ProjectConfig(ProjectBaseConfig):

    def __init__(self, configuration):
        self.config = configuration

    def get_config(self):
        return self.config


raw_config = configparser.ConfigParser()
raw_config.read(check_and_get_config_path())
config = ProjectConfig(raw_config)
