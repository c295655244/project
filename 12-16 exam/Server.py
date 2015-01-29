#/usr/bin/python
#encoding:utf-8
import socket
#服务器端
address = ('127.0.0.1', 10086) 
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.bind(address)#绑定地址
sock.listen(5)  #设置最多监听数
ss,addr=sock.accept()#等待连接
print 'got connected from',addr 
ss.send('http://exposure.anquan.org/exposure/?tab=fraud')
print '已发送网址到客户端!'

ss.close()
sock.close()
