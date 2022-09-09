from server.web.endpoint.endpoint import test_handler
from server.web.web_server import WebServer


def register_handlers(web_server: WebServer):
    web_server.get_underlying_server().add_route(test_handler, "/test", methods=["GET"])
