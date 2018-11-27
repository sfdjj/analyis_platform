# Created by wenchao.jia on 2018/11/27.
# Mail:wenchao.jia@qunar.com


# 需要进行代理的方法前缀
PROXIED_METHODS = ('insert', 'update', 'delete', 'select', 'get', 'count')

# 写操作的方法
WRITE_METHODS = ('insert', 'update', 'delete')

class Meta(type):
    def __new__(mcs, name,bases,namespace):
        cls = type.__new__(mcs,name,bases,namespace)
        wrapped_methods = []
        for k in namespace.keys():
            prefix = k.spit('_',1)[0]
            if prefix in PROXIED_METHODS:
                _fn = getattr(cls,k)
                wrapped_methods.append(_fn.__qualname__)
                write_operation = prefix in WRITE_METHODS
                new_fn =

class Dao(metaclass=Meta):


class _BaseDao(Dao)