from sanic import Blueprint

from server.common.factory import web_server
from server.web.endpoint.branch_endpoint import branch_blueprint
from server.web.endpoint.employee_endpoint import employee_blueprint
from server.web.endpoint.maintenance_endpoint import maintenance_blueprint
from server.web.endpoint.product_endpoint import product_blueprint
from server.web.endpoint.supplier_endpoint import supplier_blueprint
from server.web.exception_handler import exception_handler_blueprint
from server.web.endpoint.sale_endpoint import sale_blueprint


def web_server_run():
    api = Blueprint.group(employee_blueprint, branch_blueprint, supplier_blueprint, exception_handler_blueprint,
                          maintenance_blueprint, product_blueprint, sale_blueprint)

    web_server.get_underlying_server().blueprint(api)

    web_server.run()


def main():
    web_server_run()


if __name__ == '__main__':
    main()
