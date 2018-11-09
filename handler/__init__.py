from tornado import web as tornado_web, websocket, web


class BaseRequestHandler(tornado_web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.session = None
        self.json_data = None
        self.request_body = None
        self.proxy = False


class Route:
    def __init__(self, url: str, proxy=False):
        self.url = url
        self.proxy = proxy
