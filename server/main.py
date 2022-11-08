from logging import info

from sanic import Blueprint

from server.common.factory import web_server
from server.common.logger import configure_logging
from server.web.endpoint.branch_endpoint import branch_blueprint
from server.web.endpoint.employee_endpoint import employee_blueprint
from server.web.endpoint.exception_handler import exception_handler_blueprint
from server.web.endpoint.supplier_endpoint import supplier_blueprint


def main():
    configure_logging()
    info('test')
    api = Blueprint.group(employee_blueprint, branch_blueprint, supplier_blueprint,
                          exception_handler_blueprint)

    web_server.get_underlying_server().blueprint(api)

    web_server.run()


if __name__ == '__main__':
    main()
