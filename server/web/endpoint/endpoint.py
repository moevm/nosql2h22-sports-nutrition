from logging import debug

from bson import ObjectId
from sanic import response as res, Request, HTTPResponse

from server.common.exceptions import InvalidObjectId
from server.common.factory import employees_service


async def insert_employee(request: Request) -> HTTPResponse:
    debug(f"add_employee: {request.json}")
    return res.json(body={"id": str((await employees_service.insert(request.json)).inserted_id)})


async def get_employee_by_id(request: Request, employee_id: str) -> HTTPResponse:
    debug(f"get_employee_by_id: {employee_id}")

    check_object_id(employee_id)

    return res.json(await employees_service.find(employee_id))


def check_object_id(id: str):
    if not ObjectId.is_valid(id):
        raise InvalidObjectId(id)
