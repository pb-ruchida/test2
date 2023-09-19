import sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/sample',)

def sample(data):
    res = {'StatusCode': '200', 'XxxxxXxxxxxxXxxx': 'xxx########'}
    return res

with SimpleXMLRPCServer(('0.0.0.0', 9090), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(sample, 'xxx.xxxxx.xxxxXxxxxXxxx')
    server.serve_forever()

