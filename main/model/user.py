# Created by wenchao.jia on 2018/11/27.
# Mail:wenchao.jia@qunar.com
from peewee import PrimaryKeyField, TextField, Proxy

from main.model import BaseModel, AnalysisPaltformDb

_DB_PROXY = Proxy()

def init_db_proxy():
    _DB_PROXY.initialize(AnalysisPaltformDb().db)

class User(BaseModel):
    id = PrimaryKeyField()

    user_name = TextField()
    password = TextField()
    salt = TextField()
    email = TextField()
    tel = TextField()

    class Meta:
        db_table = 'user'

