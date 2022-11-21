from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint

from server.common.factory import branch_service, web_server
from server.data.dto_mapper import dto_indexed_from_employee_indexed
from server.web.cors.setup import setup_cors

employee_blueprint = Blueprint("employee")
app = web_server.get_underlying_server()
setup_cors(app)

@app.route("/employee/<employee_id:str>", methods=['GET'])
async def get_employee_by_id(request: Request, employee_id: str) -> HTTPResponse:
    employee_id = ObjectId(employee_id)

    info(f"get_employee_by_id: {employee_id}")

    employee = dto_indexed_from_employee_indexed(await branch_service.find_employee_by_id(ObjectId(employee_id)))

    info(f"found employee {employee}")

    return res.json(employee.dict(by_alias=True))
