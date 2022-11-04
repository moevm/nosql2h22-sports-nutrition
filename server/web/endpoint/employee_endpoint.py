from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.exceptions import InvalidObjectId
from server.common.factory import employees_service, web_server
from server.data.dto.employee_dto import EmployeeDto
from server.data.dto.insert_employee_response import InsertEmployeeResponse
from server.data.dto_mapper import dto_indexed_from_employee_indexed
from server.data.services.employee import from_employee_dto

employee_blueprint = Blueprint("employee")
app = web_server.get_underlying_server()


@app.route("/employee", methods=['POST'])
@validate(json=EmployeeDto)
async def insert_employee(request: Request, body: EmployeeDto) -> HTTPResponse:
    info(f"add_employee: {body}")

    inserted = await employees_service.insert(from_employee_dto(body))

    info(f"added employee id {inserted.inserted_id}")

    return res.json(InsertEmployeeResponse(inserted.inserted_id).__dict__)


@app.route("/employee/<employee_id:str>", methods=['GET'])
async def get_employee_by_id(request: Request, employee_id: str) -> HTTPResponse:
    check(employee_id)

    info(f"get_employee_by_id: {employee_id}")

    employee = dto_indexed_from_employee_indexed(await employees_service.find(ObjectId(employee_id)))

    info(f"found employee {employee}")

    return res.json(employee.dict())


def check(object_id: str):
    if not ObjectId.is_valid(object_id):
        raise InvalidObjectId(object_id)
