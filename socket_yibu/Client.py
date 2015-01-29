#/usr/bin/python
#encoding:utf-8
import socket
#服务器端
address_ser = ('127.0.0.1',10086)
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#函数 socket.socket 创建了一个 Socket，并返回 Socket 的描述符可用于其他 Socket 相关的函数。
#地址簇 : AF_INET (IPv4)
#类型: SOCK_STREAM (使用 TCP 传输控制协议)   
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.connect(address_ser) #向服务器建立连接
#sock.setblocking(0)
while True:
    send = raw_input('请输入信息(end结束):')
    sock.send(send)
    if send=='end':
        print '已从服务器断开'
        break
    while 1:
         get=sock.recv(1024)
         #if not get
            #print '需要接收信息后才可发送'
         #else:
         print '对方回复:', get
         break
sock.close()
