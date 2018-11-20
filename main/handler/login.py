from main.handler import BaseRequestHandler, Route


@Route(r'/login')
class Login(BaseRequestHandler):
    async def post(self,username):
        self.write(username)
