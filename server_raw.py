from tornado import web
from tornado.options import define, options


def define_options():
    define("port", type=int, help="端口号", default=8080)


def init_server():
    from handler import Route
    routes = Route.routes
    web.Application(routes).listen(8080)


def start():
    init_server()
