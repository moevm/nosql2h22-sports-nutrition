from server.common.factory import web_server
from server.common.logger import configure_logging
from server.web.endpoint.dispatcher import register_handlers
from server.web.web_server import WebServer


def main(web_server: WebServer):
    configure_logging()
    register_handlers(web_server)
    web_server.run()


if __name__ == '__main__':
    main(web_server)
