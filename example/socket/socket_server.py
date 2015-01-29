#!/usr/bin/python
# coding: utf-8
#-*- coding:gbk-*-
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))
sock.listen(5)

while True:

	connection,address = sock.accept()
	
	try:
		connection.settimeout(15)
		buf = connection.recv(1024)
		print buf
		senddata = raw_input("senddata:")
		connection.send(senddata)

		
	except socket.timeout:
		print 'time out'
	
	connection.close()
