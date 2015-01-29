#/usr/bin/python
#encoding = utf-8

import re
import urllib2
import MySQLdb
import hashlib

def run(website):
	num = 0
	db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="url360")
	webinfo = urllib2.urlopen(website).read()
	partten = re.compile('<li class=".+?"><a class=".+?" href="/url/(.+?)\.html" title=".+?">.+?</a></li>')
	datalist = partten.findall(webinfo)
	#with db:
	cursor = db.cursor()
	for dlist in datalist:
		print "url:%s"%dlist
		hashnum = hash(dlist)
		print "hash:",hashnum
		sql1 = "select url from phishurl where class ='%s'"%hashnum
		cursor.execute(sql1)
		dcount = int(cursor.rowcount)
		print "num:",dcount
		if dcount == 0:
			print "new data!"
			try:
				sql2 = "insert into phishurl (class,url) values('%s','%s')"%(hashnum,dlist)
				cursor.execute(sql2)
				#db.commit()
				num += 1
			except MySQLdb.Error,e:
				#db.rollback()
				print "wrong %d: %s"%(e.args[0],e.args[1])
		else:
			durl = cursor.fetchone()[0]
			print "the url is in the database:",durl
			if durl != dlist:
				print "!!!!! not the same!!!!!"
	db.commit()
	db.close()
	print "snum:",num

if __name__ == '__main__':
	web = "http://webscan.360.cn/url"
	run(web)


