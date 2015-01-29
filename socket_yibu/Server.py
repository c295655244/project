#/usr/bin/python
#encoding:utf-8
import socket
import threading
# 处理中文数据用的
def HKServer(client, addr, clients):
     #通知已有的每个客户，有新的成员加入
     print addr, '已加入!'
     #client.setblocking(0) 
     #接受客户端数据
     while True:
         data = client.recv(1024)
         if not data: break
         # 如果不是回车键
         if data =='end':
             print addr, '已断开!'
             break
         print '来自', addr, '的消息:', data
         send = raw_input('请输入回复信息:')
         client.send(send)
     # 把客户端发来的内容发给所有的客户端 
     #for c in clients:
     # c.send(bytes("[%s]:%s\r\n" % (addr[1], say.decode(encoding)), encoding))
     # 内容归\x0
     # 客户离开后，从客户列表中移队当前客户，关闭socket连接
     clients.remove(client)
     client.close()
     #通知已有的每个客户，有成员离开
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
