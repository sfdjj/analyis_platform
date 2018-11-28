# Created by wenchao.jia on 2018/11/27.
# Mail:wenchao.jia@qunar.com
from peewee import PrimaryKeyField, TextField, Proxy, MySQLDatabase, Model

from main.model import BaseModel, AnalysisPlatformDb

_DB_PROXY = Proxy()

def init_db_proxy():
    _DB_PROXY.initialize(AnalysisPlatformDb().db)

class User(Model):
    id = PrimaryKeyField()

    user_name = TextField()
    password = TextField()
    salt = TextField()
    email = TextField()
    tel = TextField()

    class Meta:
        database = AnalysisPlatformDb().db

