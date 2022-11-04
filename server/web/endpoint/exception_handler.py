import logging

from sanic import Blueprint
from sanic.exceptions import InvalidUsage

from server.common.factory import web_server

exception_handler_blueprint = Blueprint("exception_handler")
app = web_server.get_underlying_server()


@app.exception(ValueError)
async def exception_handler(request, exception):
    logging.exception(exception)
    raise InvalidUsage(str(exception))
