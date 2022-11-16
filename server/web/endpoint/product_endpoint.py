from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import web_server, supplier_service
from server.data.dto.product.product_dto import InsertProductWithDescriptorDto
from server.data.dto.response_dto import insert_product_response
from server.data.services.product.product import from_insert_product_with_descriptor_dto

product_blueprint = Blueprint("product")
app = web_server.get_underlying_server()


@app.route("/product/<supplier_id:str>", methods=['POST'])
@validate(json=InsertProductWithDescriptorDto)
async def insert_product_with_descriptor(request: Request,
                                         body: InsertProductWithDescriptorDto,
                                         supplier_id: str) -> HTTPResponse:
    supplier_id = ObjectId(supplier_id)

    info(f'insert new product to supplier {supplier_id}: {body}')

    service_request = from_insert_product_with_descriptor_dto(body)

    inserted_id = await supplier_service.products(supplier_id).insert_with_descriptor(service_request)

    return res.json(insert_product_response(inserted_id).dict(by_alias=True))
