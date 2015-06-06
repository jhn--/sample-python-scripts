#! /usr/bin/env python

'''
this script is a translation of a bash version first written a couple of months back.
what this script does is to dump a mysql table in a delimited format, and send it to a remote server via ftp
'''

import os
import csv
import MySQLdb
from datetime import datetime

#database (mysql) related variables
mysqlu = "test"
mysqlp = "12qwaszx"
logdir = "/var/log"
dumpdir = "/dumpdir"
datum = datetime.now().strftime("%d.%b.%Y-%H.%M")
resultfile = "resultfile."+datum+".txt"

#sftp related variables
sftpu = "sftp_user"
database_ip = "127.0.0.1"

#ftp related variables
ftpip = "127.0.0.1"
ftpu = "ftp_u"
ftpp = "ftp_pwd"
ftpdir = "ftp-dir/"

def _extraction_(mysqlu, mysqlq, database_ip, dumpdir, resultfile):
	try:

		targetfile = open(dumpdir+"/"+resultfile, 'wb')

		query = ("select * from table1")

		db = MySQLdb.connect(user = mysqlu, password = mysqlp, host = database_ip, database = "rooney_gm_trn_user_0")
		cursor = db.cursor()
		db.execute(query)

		result=cursor.fetchall()

		writing = csv.writer(targetfile, delimiter = ',')
		
		for result_row in result:
			writing.writerow(result_row)

	except MySQLdb.OperationalError, message:
		print "MySQL related error: ", message