from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import branch_service
from server.data.dto.branch.branch_dto import InsertBranchDto, BranchQueryDto, AddProductDto, InsertEmployeeDto, \
    EmployeeInBranchQueryDto, StockInBranchQueryDto
from server.data.dto.common.page_dto import PageDto
from server.data.dto.common.response_dto import response_find_branch, response_find_page, response_find_employees, \
    response_find_stocks
from server.data.dto_to_service_mapper import from_query_dto, from_employee_dto, from_employee_in_branch_query_dto, \
    from_insert_branch_dto, from_add_product_dto, from_stock_in_branch_query_dto
from server.data.service_to_dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_stock_indexed, \
    dto_indexed_from_employee_indexed, dto_info_from_branch_info
from server.data.services.common.page import from_page_dto

branch_blueprint = Blueprint("branch")


@branch_blueprint.route("/branch", methods=['POST'])
@validate(json=InsertBranchDto)
async def insert_branch(request: Request, body: InsertBranchDto) -> HTTPResponse:
    return res.json(dto_indexed_from_branch_indexed(await branch_service.insert(from_insert_branch_dto(body)))
                    .dict(by_alias=True))


@branch_blueprint.route("/branch", methods=['GET'])
@validate(query=BranchQueryDto)
async def find_branch(request: Request, query: BranchQueryDto) -> HTTPResponse:
    return res.json(response_find_branch(await branch_service.find_branches(from_query_dto(query))).dict(by_alias=True))


@branch_blueprint.route("/branch/<branch_id:str>/employee", methods=['POST'])
@validate(json=InsertEmployeeDto)
async def insert_employee(request: Request, branch_id: str, body: InsertEmployeeDto) -> HTTPResponse:
    inserted = await (await branch_service.employees(ObjectId(branch_id))).insert(from_employee_dto(body))

    return res.json(dto_indexed_from_employee_indexed(inserted).dict(by_alias=True))


@branch_blueprint.route("/branch/<branch_id:str>/employee", methods=['GET'])
@validate(query=EmployeeInBranchQueryDto)
async def find_employee(request: Request, branch_id: str, query: EmployeeInBranchQueryDto) -> HTTPResponse:
    inserted = await (await branch_service.employees(ObjectId(branch_id))) \
        .find(from_employee_in_branch_query_dto(query))

    return res.json(response_find_employees(inserted).dict(by_alias=True))


@branch_blueprint.route("/branch/<branch_id:str>/stock", methods=['GET'])
@validate(query=StockInBranchQueryDto)
async def find_stock(request: Request, branch_id: str, query: StockInBranchQueryDto) -> HTTPResponse:
    inserted = await (await branch_service.stocks(ObjectId(branch_id))).find(from_stock_in_branch_query_dto(query))

    return res.json(response_find_stocks(inserted).dict(by_alias=True))


@branch_blueprint.route("/branch/<branch_id:str>/stock", methods=['POST'])
@validate(json=AddProductDto)
async def add_product(request: Request, branch_id: str, body: AddProductDto):
    stock = await (await branch_service.stocks(ObjectId(branch_id))).add(from_add_product_dto(body))

    return res.json(dto_indexed_from_stock_indexed(stock).dict(by_alias=True))


@branch_blueprint.route("/branch/page", methods=['GET'])
@validate(query=PageDto)
async def get_page(request: Request, query: PageDto) -> HTTPResponse:
    branches = [dto_info_from_branch_info(document) for document in
                await branch_service.page_info(from_page_dto(query))]

    return res.json(response_find_page(query, branches).dict(by_alias=True))
