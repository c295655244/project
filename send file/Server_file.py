#/usr/bin/python
#encoding:utf-8
import socket
import time
import struct
import os
import threading
# 处理中文数据用的
def HKServer(conn, addr, clients):
    print '客户端加入!'
    FileInfoSize=struct.calcsize('128s32sI8s')
    FileHead=conn.recv(FileInfoSize)
    filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',FileHead)
    print '文件名:', filename,' 长度:', len(filename),' 类型:', type(filename)
    print filesize
    filename='new_'+filename.strip('\00')
    fp = open(filename,'wb')
    restsize=filesize
    while 1:
        if restsize<1024:
            filedata=conn.recv(restsize)
        else:
            filedata=conn.recv(1024)
        if not filedata:
            break
        fp.write(filedata)
        restsize=restsize-len(filedata)
        if restsize==0:break
    fp.close()
    print '接收完成!已存入 ', filename, ' 中````'

# 客户端列表
clients =[]
# 设置IP地址与端口
address_ser = ('127.0.0.1',10086)
# 初始化socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP地址与端口
s.bind(address_ser)
# 开始监听
s.listen(5)
print '服务器建立成功!' 
# 循环等待
while True:
     client, addr = s.accept()
  # 启动新的进程与客户通信
     thread = threading.Thread(target=HKServer, args=(client, addr, clients))
     thread.start()
  # 记录新的客户
     clients.append(client)
