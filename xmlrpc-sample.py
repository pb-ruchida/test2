import sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

args = sys.argv
ip = ''

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/sample',)
    def __init__(self, request, client_address, server):
        global ip
        ip = client_address[0]
        print(args[1])
        SimpleXMLRPCRequestHandler.__init__(self, request, client_address, server)

def sample(data):
    res = {'StatusCode': ip, 'XxxxxXxxxxxxXxxx': 'xxx########'}
    return res

with SimpleXMLRPCServer(('0.0.0.0', 9090), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(sample, 'xxx.xxxxx.xxxxXxxxxXxxx')
    server.serve_forever()

