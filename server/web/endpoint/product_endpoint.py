from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import product_service
from server.data.dto.common.response_dto import response_find_product
from server.data.dto.supplier.supplier_dto import ProductQueryDto
from server.data.dto_to_service_mapper import from_product_query_dto

product_blueprint = Blueprint("product")


@product_blueprint.route("/product", methods=['GET'])
@validate(query=ProductQueryDto)
async def find_supplier(request: Request, query: ProductQueryDto) -> HTTPResponse:
    return res.json(response_find_product(await product_service.find(from_product_query_dto(query)))
                    .dict(by_alias=True))
