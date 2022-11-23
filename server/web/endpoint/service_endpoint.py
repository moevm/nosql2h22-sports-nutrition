from sanic import response as res, Request, HTTPResponse, Blueprint

from server.common.factory import maintenance_service
from server.data.dto.common.response_dto import response_find_branch, response_find_supplier

service_blueprint = Blueprint("service")


@service_blueprint.route('/service/branch', methods=['GET'])
async def get_all_branches(request: Request) -> HTTPResponse:
    return res.json(response_find_branch(await maintenance_service.get_branches()).dict(by_alias=True))


@service_blueprint.route('/service/supplier', methods=['GET'])
async def get_all_suppliers(request: Request) -> HTTPResponse:
    return res.json(response_find_supplier(await maintenance_service.get_suppliers()).dict(by_alias=True))
