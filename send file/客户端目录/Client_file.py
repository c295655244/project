#/usr/bin/python
#encoding:utf-8
import socket
import time
import struct
import os
#服务器端
address_ser = ('127.0.0.1',10086)
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.connect(address_ser) #向服务器建立连接
filename=raw_input('请输入文件名:')
FileHead=struct.pack('128s11i',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
sock.send(FileHead)
fp=open(filename,'rb')
while 1:
    FileData=fp.read(1024)
    if not FileData: 
        break
    sock.send(FileData)
fp.close()
print '发送完成!已从服务器断开```````````````'
sock.close()
