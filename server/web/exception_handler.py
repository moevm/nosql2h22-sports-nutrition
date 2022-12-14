import logging

import sanic.exceptions
from bson.errors import InvalidId
from sanic import response as res, Blueprint

from server.common.factory import web_server

exception_handler_blueprint = Blueprint("exception_handler")
app = web_server.get_underlying_server()


def create_response(description: str, message: str, status: int) -> res:
    return res.json({
        'description': description,
        'status': status,
        'message': message
    },
        status=status,
        headers={"Access-Control-Allow-Origin": "*"})


def create_from_code(status: int, message: str):
    return create_response(sanic.exceptions.STATUS_CODES.get(status).decode(), message, status)


def create_invalid_usage(exception) -> res:
    return create_from_code(400, str(exception))


@app.exception(InvalidId)
async def invalid_object_id_handler(request, exception):
    logging.exception(exception)
    return create_invalid_usage(exception)


@app.exception(ValueError)
async def exception_handler(request, exception):
    logging.exception(exception)
    return create_invalid_usage(exception)
