#/usr/bin/python
#encoding:utf-8
import socket
#服务器端
address = ('127.0.0.1', 10086) 
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#函数 socket.socket 创建了一个 Socket，并返回 Socket 的描述符可用于其他 Socket 相关的函数。
#地址簇 : AF_INET (IPv4)
#类型: SOCK_STREAM (使用 TCP 传输控制协议)   
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.bind(address)#绑定地址
sock.listen(5)  #设置最多监听数
ss,addr=sock.accept()#等待连接
print 'got connected from',addr 
ss.send('已连接!\n')
while True:   
    out=ss.recv(512)
    print out
ss.close()
sock.close()
