#/usr/bin/python
#encoding:utf-8
import socket
import threading
import urllib2
import re
# 处理中文数据用的
def HKServer(client, addr, clients):
     print addr, '已加入!'
     print '已发送网址到客户端!'
     filename=client.recv(1024)
     if filename=='欺诈.txt':
         client.send('http://exposure.anquan.org/exposure/?tab=fraud')
         print 'http://exposure.anquan.org/exposure/?tab=fraud'
     elif filename=='假冒.txt':
         client.send('http://exposure.anquan.org/exposure/?tab=fake')
         print 'http://exposure.anquan.org/exposure/?tab=fake'
     elif filename=='违法违规.txt':
         client.send('http://exposure.anquan.org/exposure/?tab=illegal')
         print 'http://exposure.anquan.org/exposure/?tab=illegal'
     f=open(filename,'a+')
     print '正在接收来自客户端的信息,请稍候.....'
     while 1:
         url=client.recv(1024)
         print url
         if url=='end':
             break
         f.write(url)
         f.write("\n")
     clients.remove(client)
     client.close()
     f.close
     #通知已有的每个客户，有成员离开
     print '接收完成!可以查看当前目录下的',filename,'文件\n',
     print addr, '已离开!'
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
