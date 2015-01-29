#!/usr/bin/python
# coding: utf-8
#-*- coding:gbk-*-

import threading
import socket

buf = ''

class ThreadRecv(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.sock = sock
	
	def run(self):
		while True:
			data = self.sock.recv(1024)
			print data
	
class ThreadSend(threading.Thread):
	def __init__(self,sock):
		threading.Thread.__init__(self)
		self.sock = sock
		
	def run(self):
		while True:
			buf = raw_input()
			self.sock.send(buf)  
		
if __name__ == '__main__':
    
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	sock.connect(('localhost', 8002))  

	recv = ThreadRecv(sock)
	send = ThreadSend(sock)
	send.start()
	recv.start()


