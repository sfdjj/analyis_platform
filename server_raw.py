from tornado import web
from tornado.options import define, options
from tornado.ioloop import IOLoop


def define_options():
    define("domain", type=str, help="服务域名", default='')
    define("port", type=int, help="端口号", default=8080)


def init_server():
    from handler import Route
    routes = Route.routes
    print(routes)
    web.Application(routes).listen(options.port)

def start_event_loop():
    IOLoop.current().start()

def start():
    define_options()
    init_server()
    start_event_loop()
