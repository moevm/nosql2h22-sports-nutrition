from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import supplier_service
from server.data.dto.common.page_dto import SupplierPageDto
from server.data.dto.common.response_dto import response_find_page, response_find_supplier, response_find_product
from server.data.dto.product.product_dto import InsertProductWithDescriptorDto
from server.data.dto.supplier.supplier_dto import InsertSupplierDto, SupplierQueryDto, ProductInSupplierQueryDto
from server.data.dto_to_service_mapper import from_insert_supplier_dto, from_insert_product_with_descriptor_dto, \
    from_supplier_query_dto, from_product_in_supplier_query_dto
from server.data.service_to_dto_mapper import dto_indexed_from_supplier, dto_indexed_from_product_indexed, \
    dto_info_from_supplier
from server.data.services.common.page import from_supplier_page_dto

supplier_blueprint = Blueprint("supplier")


@supplier_blueprint.route("/supplier", methods=['POST'])
@validate(json=InsertSupplierDto)
async def insert_supplier(request: Request, body: InsertSupplierDto) -> HTTPResponse:
    return res.json(dto_indexed_from_supplier(await supplier_service.insert(from_insert_supplier_dto(body)))
                    .dict(by_alias=True))


@supplier_blueprint.route("/supplier/page", methods=['GET'])
@validate(query=SupplierPageDto)
async def get_page(request: Request, query: SupplierPageDto) -> HTTPResponse:
    suppliers = [dto_info_from_supplier(document) for document in
                 await supplier_service.page(from_supplier_page_dto(query))]

    return res.json(response_find_page(query, suppliers).dict(by_alias=True))


@supplier_blueprint.route("/supplier", methods=['GET'])
@validate(query=SupplierQueryDto)
async def find_supplier(request: Request, query: SupplierQueryDto) -> HTTPResponse:
    return res.json(response_find_supplier(await supplier_service.find(from_supplier_query_dto(query)))
                    .dict(by_alias=True))


@supplier_blueprint.route("/supplier/<supplier_id:str>/product", methods=['POST'])
@validate(json=InsertProductWithDescriptorDto)
async def insert_product_with_descriptor(request: Request,
                                         body: InsertProductWithDescriptorDto,
                                         supplier_id: str) -> HTTPResponse:
    supplier_id = ObjectId(supplier_id)

    info(f'insert new product to supplier {supplier_id}: {body}')

    inserted = await (await supplier_service.products(supplier_id)) \
        .insert_with_descriptor(from_insert_product_with_descriptor_dto(body))

    return res.json(dto_indexed_from_product_indexed(inserted).dict(by_alias=True))


@supplier_blueprint.route("/supplier/<supplier_id:str>/product", methods=['GET'])
@validate(query=ProductInSupplierQueryDto)
async def find_product(request: Request, query: ProductInSupplierQueryDto, supplier_id: str) -> HTTPResponse:
    supplier_id = ObjectId(supplier_id)

    return res.json(response_find_product(await(await supplier_service.products(supplier_id))
                                          .find(from_product_in_supplier_query_dto(query)))
                    .dict(by_alias=True))
