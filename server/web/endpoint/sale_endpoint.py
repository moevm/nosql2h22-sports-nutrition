from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.data.dto.sale.sale_dto import InsertSaleDto, SaleQueryDto


sale_blueprint = Blueprint("sale")

@sale_blueprint.route("/sale", methods=['POST'])
@validate(json=InsertSaleDto)
async def insert_sale(request: Request, body: InsertSaleDto) -> HTTPResponse:
    return res.json({})


@sale_blueprint.route("/sale", methods=['GET'])
@validate(query=SaleQueryDto)
async def find_sale(request: Request, query: SaleQueryDto) -> HTTPResponse:
    return res.json({})
