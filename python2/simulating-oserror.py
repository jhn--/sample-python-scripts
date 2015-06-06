#! /usr/bin/env python

import os, random
from datetime import datetime

def simulatingOSError():
	thisishere = os.getcwd()
	print "The folder were we are right now %s. " % (thisishere)
	randomlygeneratedfilenamewhichshouldntexistandisgoingtobedeleted = str(random.random())
	print "The randomly generated file name which we are going to delete is %s." % (randomlygeneratedfilenamewhichshouldntexistandisgoingtobedeleted)
	print "The full path where the imaginary file resides: \'%s\'." % (os.path.join(thisishere, randomlygeneratedfilenamewhichshouldntexistandisgoingtobedeleted))
	print "Deleting a file which isn't suppose to exist, right now, %s" % (str(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')))
	try:
		os.remove(os.path.join(thisishere, randomlygeneratedfilenamewhichshouldntexistandisgoingtobedeleted))
	#except OSError as (OSError[0], OSError[1]): 					#doesn't work
	#	print OSError[0], OSError[1]								#doesn't work
	except OSError as (a, b):
		print "This is the error number: '%d'." % a
		print "This is the error message: '%s'."% b
	finally:
		print '\n'\
		'As we can see, this script only generates error number 2.\n' \
		'Well, what I am concern with is the following syntax.\n' \
		'	except OSError as (errno, strerror):\n' \
		'	This is the error number: %d. % errno\n' \
		'	print This is the error message: %s. % strerror\n'

if __name__ == '__main__':
	print "This application simulates OSError. How it does it is to remove a randomly generated filename in current directory."
	simulatingOSError()