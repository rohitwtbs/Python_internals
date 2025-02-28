from twisted.web import resource, server
import json

class Json_encoder():
    pass

class UserResource():
    pass

class SumResource():
    pass

class ApiRouter(resource.Resource):
    def __init__(self):
        super().__init__()
        self.putChild(b"user",UserResource)
        self.putChild(b"sum",SumResource)


site = server.Site(ApiRouter())
