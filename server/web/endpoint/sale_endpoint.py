from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import sale_service
from server.data.dto.sale.sale_dto import InsertSaleDto, SaleQueryDto
from server.data.dto_to_service_mapper import  from_insert_sale_dto, from_sale_query_dto
from server.data.service_to_dto_mapper import dto_indexed_from_sale_indexed
from server.data.dto.common.response_dto import response_find_sale
from server.data.datetime_formatter import get_string
import datetime

sale_blueprint = Blueprint("sale")

@sale_blueprint.route("/sale", methods=['POST'])
@validate(json=InsertSaleDto)
async def insert_sale(request: Request, body: InsertSaleDto) -> HTTPResponse:
    body.date = get_string(datetime.datetime.now())
    return res.json(dto_indexed_from_sale_indexed(await sale_service.insert(from_insert_sale_dto(body))).dict(by_alias=True))

@sale_blueprint.route("/sale", methods=['GET'])
@validate(query=SaleQueryDto)
async def find_sale(request: Request, query: SaleQueryDto) -> HTTPResponse:
    return res.json(response_find_sale(await sale_service.find_sales(from_sale_query_dto(query))).dict(by_alias=True))

@sale_blueprint.route("/get_all_sales", methods=['GET'])
async def get_all_sale(request: Request) -> HTTPResponse:
    all_sales = await sale_service.get_all_sales()
    return res.json(all_sales)
