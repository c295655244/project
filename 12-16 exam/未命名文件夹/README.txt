考核题目文件 By 陈晨--130401010


一.运行环境:ubuntu.   语言:python


二.设计思想:
1.利用socket另服务器与客户端之间建立连接,并用 threading库建立多线程,实现多个客户端向服务器发送.
2.运用urllib2库对相应网页进行爬取,利用re库正则表达式进行匹配,将其逐条法向服务器
3.由于测试环境问题,爬取过多页数会造成假死现象,因此只爬取当前页面到第10页,若环境允许,可删去相应控制到第十页的代码,实现全部爬取.
4.在程序测试的过程中出现粘包现象,特此使用sleep方法解决



三.使用方法:
1.首先在ubuntu环境下运行Server_html,等待显示服务器建立成功后可以打开服务器端.
2.打开三个相应服务器端文件,若连接服务器成功则提示成功,程序将自动爬取网页并将网址存入文件


