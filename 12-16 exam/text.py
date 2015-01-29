#/usr/bin/python
#encoding:utf-8

import urllib2
import re
def spider():
    name='hehe.txt'
    html='http://www.anquan.org/seccenter/search/www.zzevp.com'
    datalists=[]
    datalist=[]
    i=1
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    htmls=html
    req = urllib2.Request(htmls, headers=headers)
    x=urllib2.urlopen(req)
    url=x.read()
       # print htmls
    try:
        partten2= re.compile(r'<div>(.+?)<span class="clr_warn">(.+?)</span>(.+?)</div>')        
        datalist = partten2.findall(url)   #利用正则表达式进行筛选
        print url
        for dlist in datalist:
                print dlist
    except EOFError:
        print '已完成!'
    print datalists
if __name__=='__main__':
    spider()

