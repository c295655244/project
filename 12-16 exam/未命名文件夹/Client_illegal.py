#/usr/bin/python
#encoding:utf-8
import socket
import urllib2
import re
import time

    
def spider(html, sock):
    datalists=[]
    datalist=[]
    i=1
    print '正在努力发送中, 请稍候.....'
    while 1:
        htmls=html+'&page='+str(i)
        x=urllib2.urlopen(htmls)
        url=x.read()
       # print htmls
        try:
            partten2= re.compile(r'<a target="_blank" href="http://www.anquan.org/s/(.+?)">.+?</a>')        
            datalist = partten2.findall(url)   #利用正则表达式进行筛选
            for dlist in datalist:
                print dlist
                sock.send(dlist)
                time.sleep(0.03)  #为了解决粘包问题,使用延迟
        except EOFError:
            print '已完成!'
            break
        #if i>10:
            #break            
        i=i+1
    sock.send('end')
    print '发送完成!可以查看当前目录下的 "违法违规.txt" 文件'
    

address_ser = ('127.0.0.1',10086)
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.connect(address_ser) #向服务器建立连接
sock.send('违法违规.txt')#发送文件名
urls=sock.recv(1024)#接收网址
spider(urls, sock)

sock.close()
