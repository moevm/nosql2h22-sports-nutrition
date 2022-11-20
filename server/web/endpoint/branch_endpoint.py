from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import web_server, branch_service
from server.data.dto.branch.branch_dto import InsertBranchDto, BranchQueryDto, AddProductDto, InsertEmployeeDto
from server.data.dto.response_dto import find_branch_response
from server.data.dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_stock_indexed, \
    dto_indexed_from_employee_indexed
from server.data.services.branch.branch import from_insert_branch_dto, from_query_dto, from_add_product_dto, \
    from_employee_dto

branch_blueprint = Blueprint("branch")
app = web_server.get_underlying_server()


@app.route("/branch", methods=['POST'])
@validate(json=InsertBranchDto)
async def insert_branch(request: Request, body: InsertBranchDto) -> HTTPResponse:
    return res.json(dto_indexed_from_branch_indexed(await branch_service.insert(from_insert_branch_dto(body)))
                    .dict(by_alias=True))


@app.route("/branch", methods=['GET'])
@validate(query=BranchQueryDto)
async def find_branch(request: Request, query: BranchQueryDto) -> HTTPResponse:
    branches = await branch_service.find_branches(from_query_dto(query))

    return res.json(find_branch_response(branches).dict(by_alias=True))


@app.route("/branch/<branch_id:str>/employee", methods=['POST'])
@validate(json=InsertEmployeeDto)
async def insert_employee(request: Request, branch_id: str, body: InsertEmployeeDto) -> HTTPResponse:
    inserted = await branch_service.employees(ObjectId(branch_id)).insert(from_employee_dto(body))

    return res.json(dto_indexed_from_employee_indexed(inserted).dict(by_alias=True))


@app.route("/branch/<branch_id:str>/product", methods=['POST'])
@validate(json=AddProductDto)
async def add_product(request: Request, branch_id: str, body: AddProductDto):
    stock = await branch_service.stocks(ObjectId(branch_id)).add(from_add_product_dto(body))

    return res.json(dto_indexed_from_stock_indexed(stock).dict(by_alias=True))
