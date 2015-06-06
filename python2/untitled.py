import MySQLdb

db = MySQLdb.connect(user='root', db='test', host='localhost')
cur = db.cursor()
cur.execute('select * from books')

z = [1,2,3]

for row in cur.fetchall():
	a = str(row[0])
	b = str(row[1])

	for i in z:
		if int(a) == i:
			print "yes " + str(b) + " is " + str(i)
#		else:
#			print "no " + str(a) + " is not" + str(i)