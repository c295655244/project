#coding=utf8

#一个简单的两人聊天软件
#服务器端


import socket, traceback, sys
host = socket.gethostbyname(socket.gethostname())            #获取本机ip地址
#host = '192.168.93.128'    
port = 8887                      #通信端口

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)              #指定最多连接数,至少为1.请求入队
s.bind((host, port))                          #将socket绑定到指定的地址上
s.listen(1)              #监听端口

ClientSock, ClientAddr = s.accept()                    #socket进入阻塞状态
while 1:                         #开始聊天
    try:
        buf = ClientSock.recv(1024)
        if len(buf):
            print u"对方 说: "+buf
        data = raw_input(u"我 说: ")
        ClientSock.sendall(data)
    except:
        print u"对话结束!"
        ClientSock.close()
        sys.exit(0)