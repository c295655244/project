from SimpleXMLRPCServer import SimpleXMLRPCServer

def add(x,y):
    return x+y

server=SimpleXMLRPCServer(("192.168.1.113",8000))
server.register_multicall_functions()
server.register_function(add,'add')

server.serve_forever()
