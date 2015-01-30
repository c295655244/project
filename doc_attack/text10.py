#coding=utf-8
''''' 
socket 给百度发送http请求 
 
连接成功后，发送http的get请求，所搜索功能 
 
'''  
import socket  
import sys  
import time  
if __name__=='__main__':  
    #创建套接字  
    try :  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    except socket.eorror,e:  
        print 'socket false:%s'%e  
    print 'socket ...'  
     
    #连接百度ip  
    try :  
        sock.connect(('172.29.153.60',80))  
    except socket.error,e:  
        print 'connect false %s'%e  
        sock.close()  
    print 'connect ...'  
     
    #发送百度首页面请求并且保持连接  
    try :  
        print 'send start...'
        str=(  
        'GET / HTTP/1.1\r\n'+
        'Host :   172.29.153.60\r\n'+
        'User-Agent:  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0\r\n'+
        'Accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'+
        'Accept-Language: zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3\r\n'+
        'Accept-Encoding: gzip, deflate\r\n'+
        'Connection : keep-alive\r\n')
        #str= "POST /a HTTP/1.1\r\n" +"HOST: " +  "172.29.153.60" + "\r\n" +"Connection: keep-alive\r\n" +"Keep-Alive: 900\r\n" +"Content-Length: 100000000\r\n" +"Content_Type: application/x-www-form-urlencoded\r\n" +"Accept: *.*\r\n"
        sock.send(str)  
    except socket.eorror,e:  
        print 'send false'  
        sock.close()  
     
    data=''  
    data = sock.recv(1024)  
    print data
    i=1
    while (1): 
        sock.send("a") 
        print 'send  %d  times' %i 
        i=i+1
        time.sleep(1000)
    #data = ''  
    #data = sock.recv(1024)     
    sock.close()  
    print data  