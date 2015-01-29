#encoding:utf-8
import MySQLdb

task_ids='1'
packetlossrates= '80%'
maxdelays ='5 ms'
averagedelays='2 ms'
lasttimes='10 s'
#                                             丢包率      最长延迟时间   平均延迟时间  攻击持续时间
def write_to_mysql(task_id, packetlossrate, maxdelay ,averagedelay, lasttime):
	task_id='1'
	try:
		db = MySQLdb.connect(host="192.168.1.117",user="tcphalf",passwd="hitwh",db="information" ,charset='utf8')
	except:
		print '数据库连接失败!'
	cursor = db.cursor()

	try:
		sqls = "update mainpage_tcphalf set packetlossrate = '%s'   where id ='%s' " %(packetlossrate,task_id)
		cursor.execute(sqls)
		sqls = "update mainpage_tcphalf set maxdelay = '%s'   where id ='%s' " %(maxdelay,task_id)
		cursor.execute(sqls)
		sqls = "update mainpage_tcphalf set averagedelay = '%s'   where id ='%s' " %(averagedelay,task_id)
		cursor.execute(sqls)
		sqls = "update mainpage_tcphalf set lasttime = '%s'   where id ='%s' " %(lasttime,task_id)
		cursor.execute(sqls)
		sqls2 = "update mainpage_tcphalf set status='1'  where id ='%s' "%task_id
		cursor.execute(sqls2)
		db.commit()
	except:
		print '写入数据库失败!'
		db.rollback()
	db.close

if __name__ == '__main__':
	task_id='1'
	reasult='已攻击1000次'
	write_to_mysql(task_ids, packetlossrates, maxdelays,averagedelays, lasttimes)

