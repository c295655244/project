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
        #print data
        if i==2:
            name=data
        if i==9:
            score=data
            if score=='' or score==' ':
                score='暂无成绩'
        if i==12:
            type='('+data+')'
        if i==13:
            print name+type+'-----成绩:'+score          
        if i==14:
            i=0
        i=i+1
 
def post(url1,url2,  data):
    req = urllib2.Request(url1)
    data = urllib.urlencode(data)
    #enable cookie
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data)
        response = opener.open(url2)
        html = unicode(response.read(), "gb2312").encode("utf8")
        spider(html)
    except:
        print '登录失败!请检查您的学号和密码!'
        main()
 
def main():
    posturl1 = "http://222.194.15.1:7777/pls/wwwbks/bks_login2.login"
    posturl2 = "http://222.194.15.1:7777/pls/wwwbks/bkscjcx.curscopre"
    number=raw_input("请输入学号:")
    password=raw_input("请输入密码:")
    data = { 'stuid':number, 'pwd':password}
    post(posturl1, posturl2, data)
 
 
if __name__ == '__main__':
    main()

