from logging import info

from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import web_server, branch_service
from server.data.dto.branch_dto import InsertBranchDto, BranchQueryDto
from server.data.dto.response_dto import insert_branch_response
from server.data.dto_mapper import dto_indexed_from_branch_indexed
from server.data.services.branch import from_insert_branch_dto, from_query_dto

branch_blueprint = Blueprint("branch")
app = web_server.get_underlying_server()


@app.route("/branch", methods=['POST'])
@validate(json=InsertBranchDto)
async def insert_branch(request: Request, body: InsertBranchDto) -> HTTPResponse:
    inserted = await branch_service.insert(from_insert_branch_dto(body))

    info(f"inserted branch id: {inserted}")

    return res.json(insert_branch_response(inserted).dict(by_alias=True))


@app.route("/branch", methods=['GET'])
@validate(query=BranchQueryDto)
async def find_branch(request: Request, query: BranchQueryDto) -> HTTPResponse:
    branches = await branch_service.find_branches(from_query_dto(query))

    return res.json([dto_indexed_from_branch_indexed(branch).dict(by_alias=True) for branch in branches])
