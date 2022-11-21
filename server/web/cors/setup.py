from sanic import Sanic
from server.web.cors.cors import add_cors_headers
from server.web.cors.options import setup_options


def setup_cors(app: Sanic):
    # Add OPTIONS handlers to any route that is missing it
    app.register_listener(setup_options, "before_server_start")
    # Fill in CORS headers
    app.register_middleware(add_cors_headers, "response")