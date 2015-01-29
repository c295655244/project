#/usr/bin/python
#encoding:utf-8
import socket
#服务器端
address = ('127.0.0.1',10086) 
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.connect(address) #向服务器建立连接
while True:
    name = raw_input('请输入信息:')
    sock.send(name)
sock.close()
