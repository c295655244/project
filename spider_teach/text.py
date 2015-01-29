#/usr/bin/env python
# -*- coding=utf-8 -*-
 
import urllib
import urllib2
import re
 
def spider(text):
    partten = re.compile(r'<td width="112" height="20" class=td_biaogexian><p align="center">(.*?)</p></td>')
    datalist = partten.findall(text)
    information=['详细信息','课程号', '课程名', '课序号', '学分', '考试时间', '实验成绩', '平时成绩', '期末成绩', '总成绩', '课程属性',
    '替代课程号','考试类型','备注']
    i=0
    for data in datalist:
        print data
def post(url1,url2,  data):
    req = urllib2.Request(url1)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    response = opener.open(url2)
    html = unicode(response.read(), "gb2312").encode("utf8")
   # if  "登陆成功"in html:
    spider(html)
    #else:
       # return '登录失败!'
 
def main():
    posturl1 = "http://222.194.15.1:7777/pls/wwwbks/bks_login2.login"
    posturl2 = "http://222.194.15.1:7777/pls/wwwbks/bkscjcx.curscopre"
    data = { 'stuid':'130410101', 'pwd':'295655244'}
    post(posturl1, posturl2, data)
 
 
if __name__ == '__main__':
    main()

