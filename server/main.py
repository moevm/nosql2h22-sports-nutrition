from sanic import Blueprint

from server.common.factory import web_server
from server.common.logger import configure_logging
from server.web.endpoint.branch_endpoint import branch_blueprint
from server.web.endpoint.employee_endpoint import employee_blueprint
from server.web.endpoint.service_endpoint import service_blueprint
from server.web.endpoint.supplier_endpoint import supplier_blueprint
from server.web.exception_handler import exception_handler_blueprint


def web_server_run():
    api = Blueprint.group(employee_blueprint, branch_blueprint, supplier_blueprint, exception_handler_blueprint,
                          service_blueprint)

    web_server.get_underlying_server().blueprint(api)

    web_server.run()


def main():
    configure_logging()
    web_server_run()


if __name__ == '__main__':
    main()
