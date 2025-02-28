from twisted.web import server, resource 
from twisted.internet import reactor

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self,request):
        return b"<html><body><h1>Hello , Twisted HTTP server </h1></body></html>"
    

site = server.Site(Simple())
reactor.listenTCP(8080, site)
print("HTTP serevr running on port 8080")
reactor.run()