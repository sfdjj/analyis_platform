from handler import Route, BaseRequestHandler


@Route(r"/helloWorld")
class HelloWorld(BaseRequestHandler):
    async def get(self):
        self.write("helloWorld")
