from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import sale_service
from server.data.dto.sale.sale_dto import InsertSaleDto, SaleQueryDto
from server.data.dto_to_service_mapper import  from_insert_sale_dto
from server.data.service_to_dto_mapper import dto_indexed_from_sale_indexed

sale_blueprint = Blueprint("sale")

@sale_blueprint.route("/sale", methods=['POST'])
@validate(json=InsertSaleDto)
async def insert_sale(request: Request, body: InsertSaleDto) -> HTTPResponse:
    return res.json(dto_indexed_from_sale_indexed(await sale_service.insert(from_insert_sale_dto(body))).dict(by_alias=True))

@sale_blueprint.route("/sale", methods=['GET'])
@validate(query=SaleQueryDto)
async def find_sale(request: Request, query: SaleQueryDto) -> HTTPResponse:
    return res.json({})