from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import maintenance_service
from server.data.dto.common.page_dto import PageDto
from server.data.dto.common.response_dto import response_find_page
from server.data.service_to_dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_supplier
from server.data.services.common.page import from_page_dto

maintenance_blueprint = Blueprint("maintenance")


@maintenance_blueprint.route("/maintenance/branch/page", methods=['GET'])
@validate(query=PageDto)
async def get_branches(request: Request, query: PageDto) -> HTTPResponse:
    branches = [dto_indexed_from_branch_indexed(document) for document in
                await maintenance_service.branch_page(from_page_dto(query))]

    return res.json(response_find_page(query, branches).dict(by_alias=True))


@maintenance_blueprint.route("/maintenance/supplier/page", methods=['GET'])
@validate(query=PageDto)
async def get_suppliers(request: Request, query: PageDto) -> HTTPResponse:
    suppliers = [dto_indexed_from_supplier(document) for document in
                 await maintenance_service.supplier_page(from_page_dto(query))]

    return res.json(response_find_page(query, suppliers).dict(by_alias=True))
