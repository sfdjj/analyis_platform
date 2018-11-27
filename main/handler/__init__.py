import functools
import json
from typing import Union

from jsonschema import Draft4Validator, ValidationError
from pydash import map_
from tornado import web as tornado_web, websocket, web

from main.common.exception import JsonValidationException


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


class JsonRequest:
    def __init__(self, schema=None, allow_none=False):
        if schema:
            self.validator = JsonValidator(schema)
        else:
            self.validator = None
        self.allow_none = allow_none

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(_self, *args, **kwargs):
            if _self.json_data is None:
                request_body = _self.request.body.decode('utf-8', errors='replace')
                _self.json_data = _deep_strip_str(loads(request_body))
                _self.request_body = request_body

            if self.validator is not None:
                self.validator.validate(_self.json_data)

            return func(_self, *args, **kwargs)

        return wrapper


class JsonValidator:
    def __init__(self, schema):
        Draft4Validator.check_schema(schema)
        self.validator = Draft4Validator(schema)

    def validate(self, data):
        try:
            self.validator.validate(data)
        except ValidationError as e:
            path = '/'.join(map(str, e.path))
            raise JsonValidationException(f'{path}:{e.message}')


def _deep_strip_str(obj: Union[str, list, dict]):
    if isinstance(obj, str):
        result = obj.strip()
    elif isinstance(obj, list):
        result = map_(obj, _deep_strip_str())
    elif isinstance(obj, dict):
        result = {_deep_strip_str(k): _deep_strip_str(v) for k, v in obj.items()}
    else:
        result = obj
    return result


def loads(s: Union[str, bytes]) -> Union[dict, list]:
    if isinstance(s, bytes):
        s = s.decode('utf-8', errors='replace')
    try:
        return json.loads(s)
    except ValueError:
        raise JsonValidationException('数据非JSON格式')
