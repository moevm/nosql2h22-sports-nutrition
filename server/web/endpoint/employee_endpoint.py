from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import branch_service, web_server
from server.data.dto.branch_dto import InsertEmployeeDto
from server.data.dto.response_dto import insert_employee_response
from server.data.dto_mapper import dto_indexed_from_employee_indexed
from server.data.services.branch import from_employee_dto

employee_blueprint = Blueprint("employee")
app = web_server.get_underlying_server()


@app.route("/employee/<branch_id:str>", methods=['POST'])
@validate(json=InsertEmployeeDto)
async def insert_employee(request: Request, branch_id: str, body: InsertEmployeeDto) -> HTTPResponse:
    info(f"insert employee to branch {branch_id}: {body}")

    inserted = await branch_service.employees(ObjectId(branch_id)).insert(from_employee_dto(body))

    info(f"inserted employee id {inserted}")

    return res.json(insert_employee_response(inserted).dict(by_alias=True))


@app.route("/employee/<employee_id:str>", methods=['GET'])
async def get_employee_by_id(request: Request, employee_id: str) -> HTTPResponse:
    info(f"get_employee_by_id: {employee_id}")

    employee = dto_indexed_from_employee_indexed(await branch_service.find_employee_by_id(ObjectId(employee_id)))

    info(f"found employee {employee}")

    return res.json(employee.dict(by_alias=True))
