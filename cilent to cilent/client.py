# -*- coding: utf-8 -*-
import socket
import threading
 
 
inString = ''
outString = ''
nick = ''
 
def DealOut(s):#显示函数
    global nick, outString
    while True:
        outString = raw_input()
        outString = nick + ': ' + outString
        s.send(outString)
 
def DealIn(s):#输入函数
    global inString
    while True:
        try:
            inString = s.recv(1024)
            if not inString:
                break
            if outString != inString:
                print inString
        except:
            break
         
 
nick = raw_input("input your nickname: ")#输入该客户端姓名
ip ='127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, 10086))
sock.send(nick)#发送姓名
 
thin = threading.Thread(target = DealIn, args = (sock,))
thin.start()#开启输入进程
thout = threading.Thread(target = DealOut, args = (sock,))
thout.start()#开启输出进程
 
#sock.close()
