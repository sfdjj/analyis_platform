# Created by wenchao.jia on 2018/11/27.
# Mail:wenchao.jia@qunar.com

from peewee import Model
from peewee_async import PooledMySQLDatabase
from pypattyrn.creational.singleton import Singleton
from tornado.locks import Event


class BaseModel(Model):
    initialize_event = Event()


class AnalysisPaltformDb(metaclass=Singleton):
    def __init__(self):
        self.db = PooledMySQLDatabase(host='127.0.0.1',port=3306,user='root',password='123456',
                                      database='analysis_platform',autocommit=False,threadlocals=True,
                                      max_connection=100)