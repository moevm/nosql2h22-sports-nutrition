from server.common.logger import configure_logging
from server.web.endpoint.dispatcher import register_handlers
from server.web.web_server import web_server

if __name__ == '__main__':
    configure_logging()
    register_handlers(web_server)
    web_server.run()
