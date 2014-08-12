#!/usr/bin/env python

import os, sys

path = raw_input("Enter a absolute path to a directory or a file.\
	E.g. \"/bin\" or \"/bin/chmod\". > ")

def statfile(path):
	try:
		file_stat_info = os.stat(path)
		return file_stat_info
	except OSError:
		print "OS error({0}): {1}" .format(OSError.errno, OSError.strerror)
	except:
		print "Unexpected error:", sys.exc_info()[0]

print statfile(path)