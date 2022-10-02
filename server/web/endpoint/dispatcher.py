from server.web.endpoint.endpoint import insert_employee, get_employee_by_id
from server.web.web_server import WebServer


def register_handlers(web_server: WebServer):
    web_server.get_underlying_server().add_route(insert_employee, "/employees", methods=["POST"])
    web_server.get_underlying_server().add_route(get_employee_by_id, "/employees/<employee_id:str>", methods=["GET"])
