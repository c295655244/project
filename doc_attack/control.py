#coding=utf-8
import os
import re
from subprocess import Popen, PIPE



#packetlossrate, maxdelay ,averagedelay
def control():
	orders='ping -c 3 172.29.153.60'
	resp = os.popen(orders)
	string=resp.read()
	pattern = re.compile(r'=.*?/(.*?)/(.*?)/.*?ms')
	pattern2 = re.compile(r'received, (.*?) packet loss')
	#received, (.*?) packet loss\S*?
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
	match = pattern.findall(string)
	match2=pattern2.findall(string)
	print string
	packetlossrate=match2[0]
	maxdelay=match[0][1]
	averagedelay=match[0][0]
	print packetlossrate
	print maxdelay
	print averagedelay
	#reasult= '造成该网站:  平均延迟:  %s ms ,最大延迟:  %s ms' %(match[0])
	#print reasult

if __name__ == '__main__':
        control()