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
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
       # print htmls
        try:
            partten2= re.compile(r'<a target="_blank" href="http://www.anquan.org/s/(.+?)">.+?</a>')  
            partten3= re.compile(r'<div class="risk_desc">\s*?<div>\s*?(\S*?)\s*?<span class="clr_warn">(.+?)</span>\s*?(\S*?)&nbsp;\s*?</div>')
            datalist = partten2.findall(url)   #利用正则表达式进行筛选
            for dlist in datalist:
                record=dlist
                dlist='http://www.anquan.org/seccenter/search/'+dlist
                print dlist
                req = urllib2.Request(dlist, headers=headers)
                x2=urllib2.urlopen(req)
                url2=x2.read()
                datalist2 = partten3.findall(url2)
                for data in datalist2:
                    record=record+'--'+ data[0]+data[1]+data[2]
                print  record, '--', data[0], data[1], data[2]
                sock.send(record)
                time.sleep(0.03)#为了解决粘包问题,使用延迟
        except EOFError:
            print '已完成!'
            break
        #if i>2:
            #break            
        i=i+1
    print '发送完成!可以查看当前目录下的 "欺诈.txt" 文件', 
    

address_ser = ('127.0.0.1',10086)
try:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'socket success!'
except:
    print 'socket对象建立失败!'
sock.connect(address_ser) #向服务器建立连接
sock.send('欺诈.txt')#发送文件名
urls=sock.recv(1024)#接收网址
spider(urls, sock)
sock.send('end')
sock.close()
