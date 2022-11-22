from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import web_server, branch_service
from server.data.dto.branch.branch_dto import InsertBranchDto, BranchQueryDto, AddProductDto, InsertEmployeeDto, \
    EmployeeInBranchQueryDto
from server.data.dto.common.page_dto import PageDto
from server.data.dto.common.response_dto import response_find_branch, response_find_page, response_find_employees
from server.data.dto_mapper import dto_indexed_from_branch_indexed, dto_indexed_from_stock_indexed, \
    dto_indexed_from_employee_indexed
from server.data.services.branch.branch import from_insert_branch_dto, from_query_dto, from_add_product_dto, \
    from_employee_dto, from_employee_in_branch_query_dto
from server.data.services.common.page import from_page_dto

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
    return res.json(response_find_branch(await branch_service.find_branches(from_query_dto(query))).dict(by_alias=True))


@app.route("/branch/<branch_id:str>/employee", methods=['POST'])
@validate(json=InsertEmployeeDto)
async def insert_employee(request: Request, branch_id: str, body: InsertEmployeeDto) -> HTTPResponse:
    inserted = await branch_service.employees(ObjectId(branch_id)).insert(from_employee_dto(body))

    return res.json(dto_indexed_from_employee_indexed(inserted).dict(by_alias=True))


@app.route("/branch/<branch_id:str>/employee", methods=['GET'])
@validate(query=EmployeeInBranchQueryDto)
async def find_employee(request: Request, branch_id: str, query: EmployeeInBranchQueryDto) -> HTTPResponse:
    inserted = await branch_service.employees(ObjectId(branch_id)).find(from_employee_in_branch_query_dto(query))

    return res.json(response_find_employees(inserted).dict(by_alias=True))


@app.route("/branch/<branch_id:str>/product", methods=['POST'])
@validate(json=AddProductDto)
async def add_product(request: Request, branch_id: str, body: AddProductDto):
    stock = await branch_service.stocks(ObjectId(branch_id)).add(from_add_product_dto(body))

    return res.json(dto_indexed_from_stock_indexed(stock).dict(by_alias=True))


@app.route("/branch/page", methods=['GET'])
@validate(json=PageDto)
async def get_page(request: Request, body: PageDto) -> HTTPResponse:
    branches = [dto_indexed_from_branch_indexed(document) for document in
                await branch_service.page(from_page_dto(body))]

    return res.json(response_find_page(body, branches).dict(by_alias=True))
