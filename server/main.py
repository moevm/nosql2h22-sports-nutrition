from sanic import Blueprint

from server.common.factory import web_server
from server.common.logger import configure_logging
from server.web.endpoint.employee_endpoint import employee_blueprint
from server.web.endpoint.exception_handler import exception_handler_blueprint


def main():
    configure_logging()

    api = Blueprint.group(employee_blueprint, exception_handler_blueprint)

    web_server.get_underlying_server().blueprint(api)

    web_server.run()


if __name__ == '__main__':
    main()
