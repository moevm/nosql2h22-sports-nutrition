from abc import ABC, abstractmethod

from sanic import Sanic
from sanic_cors import CORS
from sanic_ext import Extend

from server.common.common import Worker
from server.common.logger import is_logged
from server.common.web_config import ProjectConfigWeb, ServerType


class InnerServer(Worker, ABC):
    @abstractmethod
    def get_server(self):
        pass


class SanicServer(InnerServer, ABC):

    def __init__(self, config: ProjectConfigWeb):
        self.config = config
        self.server = self.create_server("sports-nutrition")

    def cors_setup(self, server):
        options = {"resources": r'/*', "origins": "*", "methods": ["GET", "POST", "HEAD", "OPTIONS"]}
        Extend(server, extensions=[CORS], config={"CORS": False, "CORS_OPTIONS": options})

    def create_server(self, server_name):
        server = Sanic(server_name)
        self.cors_setup(server)
        return server

    @is_logged()
    def run(self) -> None:
        self.server.run(host=self.config.get_host(), port=self.config.get_port(), fast=True, access_log=True)

    def stop(self) -> None:
        self.server.stop()

    def get_server(self):
        return self.server


class InnerServerFactory:
    def __init__(self):
        self.factory = {}
        self.init_factory()

    def init_factory(self):
        self.factory[ServerType.Sanic] = SanicServer

    @is_logged()
    def create(self, config: ProjectConfigWeb) -> InnerServer:
        return self.factory[config.get_server_type()](config)


class WebServer(Worker):

    def __init__(self, config: ProjectConfigWeb, factory: InnerServerFactory):
        self.config = config
        self.server = factory.create(config)

    @is_logged()
    def run(self) -> None:
        self.server.run()

    def stop(self) -> None:
        self.server.stop()

    def get_underlying_server(self):
        return self.server.get_server()
