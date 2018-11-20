from tornado import web as tornado_web, websocket, web


class BaseRequestHandler(tornado_web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.session = None
        self.json_data = None
        self.request_body = None
        self.proxy = False


class Route:
    routes = []

    def __init__(self, url: str, proxy=False):
        self.url = url
        self.proxy = proxy

    def __call__(self, handler):
        # url = '/_internal' + self.url if self.proxy else self.url
        if self.is_enabled():
            url = self.url
            self.routes.append((url, handler))
        return handler

    @staticmethod
    def is_enabled():
        return True
