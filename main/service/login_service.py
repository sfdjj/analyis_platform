# Created by wenchao.jia on 2018/11/20.
# Mail:wenchao.jia@qunar.com
from main.service import BaseService


class LoginService(BaseService):
    async def login(self,data):
        user_name = data['user_name']
        passoword = data['password']
        email = data['email']
        tel = data['tel']