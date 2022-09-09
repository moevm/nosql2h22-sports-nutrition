from logging import debug

from sanic import response as res


async def test_handler(req):
    debug(f"got a request: {req}")
    return res.text("I\'m a teapot", status=418)
