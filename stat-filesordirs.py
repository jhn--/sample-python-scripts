#!/usr/bin/env python

import os

path = raw_input("Enter a absolute path to a directory or a file.\
	E.g. \"/bin\" or \"/bin/chmod\". > ")

def statfile(path):
	try:
		file_stat_info = os.stat(path)
		return file_stat_info
	except OSError as (errno, strerror):
		return "OS Error: Error code %d. The file/directory: \"%s\". %s." % (errno, os.path.basename(path), strerror)

print statfile(path)