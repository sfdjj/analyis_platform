import os

from tornado import web
from tornado.ioloop import IOLoop
from tornado.options import define, options

from main.configuration import config


def define_options():
    define("domain", type=str, help="服务域名", default='')
    define("port", type=int, help="端口号", default=8080)


def init_server():
    from main.handler import Route
    routes = Route.routes
    print(routes)
    web.Application(routes).listen(options.port)


def import_sub_modules(dir_name):
    """
    导入该目录下的所有模块
    :param dir_name:
    :return:
    """
    for file in os.listdir(os.path.join(config.APP_ROOT_PATH, dir_name)):
        if file.startswith('_') or file.endswith('.pyc'):
            continue
        file = os.path.join(dir_name, file)
        if file.endswith('.py'):
            __import__(file[:-3].replace('/', '.'))
        else:
            __import__(file.replace('/', '.'))

        if os.path.isdir(os.path.join(config.APP_ROOT_PATH, file)):
            import_sub_modules(file)


def set_config_root():
    config.APP_ROOT_PATH = os.path.dirname(__file__)
    config.CONFIG_ROOT_PATH = os.path.join(config.APP_ROOT_PATH, 'config')


def start_event_loop():
    IOLoop.current().start()


def start():
    define_options()
    set_config_root()
    import_sub_modules('main')
    init_server()
    start_event_loop()
