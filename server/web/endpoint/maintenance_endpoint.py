from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import maintenance_service
from server.data.dto.branch.branch_indexed_dto import IndexedBranchesDto
from server.data.dto.common.page_dto import PageDto
from server.data.dto.common.response_dto import response_find_page, response_insert_ids
from server.data.dto.supplier.supplier_indexed_dto import SuppliersDto
from server.data.dto_to_service_mapper import from_branch_dto, from_supplier_dto
from server.data.service_to_dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_supplier
from server.data.services.common.page import from_page_dto

maintenance_blueprint = Blueprint("maintenance")


@maintenance_blueprint.route("/maintenance/branch/page", methods=['GET'])
@validate(query=PageDto)
async def get_branches(request: Request, query: PageDto) -> HTTPResponse:
    branches = [dto_indexed_from_branch_indexed(document) for document in
                await maintenance_service.get_branch_page(from_page_dto(query))]

    return res.json(response_find_page(query, branches).dict(by_alias=True))


@maintenance_blueprint.route("/maintenance/branch", methods=['POST'])
@validate(json=IndexedBranchesDto)
async def insert_branches(request: Request, body: IndexedBranchesDto) -> HTTPResponse:
    inserted_ids = await maintenance_service.insert_branches(list(map(from_branch_dto, body.branches)))
    return res.json(response_insert_ids(inserted_ids).dict(by_alias=True))


@maintenance_blueprint.route("/maintenance/supplier", methods=['POST'])
@validate(json=SuppliersDto)
async def insert_suppliers(request: Request, body: SuppliersDto) -> HTTPResponse:
    inserted_ids = await maintenance_service.insert_suppliers(list(map(from_supplier_dto, body.suppliers)))
    return res.json(response_insert_ids(inserted_ids).dict(by_alias=True))


@maintenance_blueprint.route("/maintenance/supplier/page", methods=['GET'])
@validate(query=PageDto)
async def get_suppliers(request: Request, query: PageDto) -> HTTPResponse:
    suppliers = [dto_indexed_from_supplier(document) for document in
                 await maintenance_service.get_supplier_page(from_page_dto(query))]

    return res.json(response_find_page(query, suppliers).dict(by_alias=True))
