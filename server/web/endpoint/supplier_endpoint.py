from logging import info

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse, Blueprint
from sanic_ext import validate

from server.common.factory import web_server, supplier_service
from server.data.dto.response_dto import insert_supplier_response
from server.data.dto.supplier.supplier_dto import InsertSupplierDto
from server.data.dto_mapper import dto_indexed_from_supplier
from server.data.services.supplier.supplier import from_insert_supplier_dto

supplier_blueprint = Blueprint("supplier")
app = web_server.get_underlying_server()


@app.route("/supplier", methods=['POST'])
@validate(json=InsertSupplierDto)
async def insert_supplier(request: Request, body: InsertSupplierDto) -> HTTPResponse:
    inserted = await supplier_service.insert(from_insert_supplier_dto(body))

    info(f"inserted supplier id: {inserted}")

    return res.json(insert_supplier_response(inserted).dict(by_alias=True))


@app.route("/supplier/<supplier_id:str>", methods=['GET'])
async def find_supplier_by_id(request: Request, supplier_id: str) -> HTTPResponse:
    supplier = dto_indexed_from_supplier(await supplier_service.find_by_id(ObjectId(supplier_id)))

    info(f"found supplier: {supplier}")

    return res.json(supplier.dict(by_alias=True))
