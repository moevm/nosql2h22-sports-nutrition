from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import branch_service
from server.data.dto.branch.branch_dto import EmployeeQueryDto
from server.data.dto.common.response_dto import response_find_employees
from server.data.dto_to_service_mapper import from_employee_query_dto

employee_blueprint = Blueprint("employee")


@employee_blueprint.route("/employee", methods=['GET'])
@validate(query=EmployeeQueryDto)
async def find_employee(request: Request, query: EmployeeQueryDto) -> HTTPResponse:
    return res.json(response_find_employees(await branch_service.find_employee(from_employee_query_dto(query)))
                    .dict(by_alias=True))
