# -*- coding: utf-8 -*-
import socket
import sys
import threading
 
con = threading.Condition()
HOST = '127.0.0.1'
PORT = 10086 
data = ''
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
s.bind((HOST, PORT))#绑定端口
s.listen(10)
print 'Socket now listening'
def clientThreadIn(conn, nick):
    global data
    while True:
        try:
            temp = conn.recv(1024)#接收信息
            if not temp:
                conn.close()#关闭客户端
                return
            NotifyAll(temp)#唤醒所有客户端,通知其运行
            print data
        except:
            NotifyAll(nick + " leaves the room!")
            print data
            return
 
def NotifyAll(sss):
    global data
    if con.acquire():
        data = sss
        con.notifyAll()#通知所有线程继续运行
        con.release()
  
def ClientThreadOut(conn, nick):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return
                     
 
while 1:
    conn, addr = s.accept()#等待接收客户端
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    nick = conn.recv(1024)#接收客户端名
    NotifyAll('Welcome ' + nick + ' to the room!')#
    print data
    print str((threading.activeCount() + 1) / 2) + ' person(s)!'#输出目前聊天室人数
    conn.send(data)
    threading.Thread(target = clientThreadIn , args = (conn, nick)).start()
    threading.Thread(target = ClientThreadOut , args = (conn, nick)).start()
 
s.close()
