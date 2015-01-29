#!/usr/bin/python
# coding: utf-8
#-*- coding:gbk-*-

import threading
import socket

buf = ''

class ThreadRecv(threading.Thread):
	def __init__(self,connection):
		threading.Thread.__init__(self)
		self.connection = connection
		
	def run(self):
		while True:
			buf = self.connection.recv(1024)
			print buf
	
class ThreadSend(threading.Thread):
	def __init__(self,connection):
		threading.Thread.__init__(self)
		self.connection = connection
	
	def run(self):
		while True:
			data = raw_input()
			self.connection.send(data)
	
if __name__ == '__main__':

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('localhost', 8002))
	sock.listen(5)

	connection,address = sock.accept()
	recv = ThreadRecv(connection)
	send = ThreadSend(connection)
	recv.start()
	send.start()
	
