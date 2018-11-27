from main.handler import BaseRequestHandler, Route, JsonRequest, _deep_strip_str, loads


@Route(r'/login')
class Login(BaseRequestHandler):
    async def post(self, username):
        self.write(username)


@Route(r'/register')
class Register(BaseRequestHandler):
    @JsonRequest({
        "properties": {
            "user_name": {"type": "string"},
            "password": {"type": "string"},
            "email": {"type": "string"},
            "tel": {"type": "string"}
        },
        "required": ["username", "password"],
        "type": "object"
    })
    async def post(self):
        data = self.json_data
        self.write(data['username'])
