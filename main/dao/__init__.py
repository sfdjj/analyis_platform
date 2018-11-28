# Created by wenchao.jia on 2018/11/27.
# Mail:wenchao.jia@qunar.com


# 需要进行代理的方法前缀
from main.configuration import Session
from main.model import AnalysisPlatformDb
from main.model.user import User
from main.service import BaseService

PROXIED_METHODS = ('insert', 'update', 'delete', 'select', 'get', 'count')

# 写操作的方法
WRITE_METHODS = ('insert', 'update', 'delete')


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        cls = type.__new__(mcs, name, bases, namespace)
        wrapped_methods = []
        for k in namespace.keys():
            prefix = k.split('_', 1)[0]
            if prefix in PROXIED_METHODS:
                _fn = getattr(cls, k)
                wrapped_methods.append(_fn.__qualname__)
                write_operation = prefix in WRITE_METHODS
                # new_fn =
                setattr(cls, k, _fn)
        return cls


# class Dao(metaclass=Meta):
class Dao:
    model = None

    def __init__(self, tx=None):

        if isinstance(tx, BaseService):
            tx = tx.session.tx

        elif isinstance(tx, Session):
            tx = tx.tx
        self.tx = tx

    @property
    def db(self):
        raise NotImplementedError()

    def insert(self, d: dict, upset=False):
        if 'id' in d:
            del d['id']

        sql = self.model.insert(**d)
        if upset:
            sql = sql.upset()
        return sql.execute()

    def select(self, model_id, fields_names: list = ()):
        return self._get_query(fields_names).where(self.model.id == model_id)

    def _get_query(self, field_names=(), *extra_fields):
        fields = []
        if not field_names:
            fields.append(self.model)
        for field_name in field_names:
            fields.append(getattr(self.model, field_name))

        return self.model.select(*fields, *extra_fields)


class _BaseDao(Dao):
    @property
    def db(self):
        return AnalysisPlatformDb().db


class UserDao(_BaseDao):
    model = User


