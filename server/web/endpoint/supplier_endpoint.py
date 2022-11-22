from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import supplier_service
from server.data.dto.product.product_dto import InsertProductWithDescriptorDto
from server.data.dto.supplier.supplier_dto import InsertSupplierDto
from server.data.dto_to_service_mapper import from_insert_supplier_dto, from_insert_product_with_descriptor_dto
from server.data.service_to_dto_mapper import dto_indexed_from_supplier, dto_indexed_from_product_indexed

supplier_blueprint = Blueprint("supplier")


@supplier_blueprint.route("/supplier", methods=['POST'])
@validate(json=InsertSupplierDto)
async def insert_supplier(request: Request, body: InsertSupplierDto) -> HTTPResponse:
    return res.json(dto_indexed_from_supplier(await supplier_service.insert(from_insert_supplier_dto(body)))
                    .dict(by_alias=True))


@supplier_blueprint.route("/supplier/<supplier_id:str>", methods=['GET'])
async def find_supplier_by_id(request: Request, supplier_id: str) -> HTTPResponse:
    return res.json(dto_indexed_from_supplier(await supplier_service.find_by_id(ObjectId(supplier_id)))
                    .dict(by_alias=True))


@supplier_blueprint.route("/supplier/<supplier_id:str>/product", methods=['POST'])
@validate(json=InsertProductWithDescriptorDto)
async def insert_product_with_descriptor(request: Request,
                                         body: InsertProductWithDescriptorDto,
                                         supplier_id: str) -> HTTPResponse:
    supplier_id = ObjectId(supplier_id)

    info(f'insert new product to supplier {supplier_id}: {body}')

    inserted = await supplier_service.products(supplier_id) \
        .insert_with_descriptor(from_insert_product_with_descriptor_dto(body))

    return res.json(dto_indexed_from_product_indexed(inserted).dict(by_alias=True))
