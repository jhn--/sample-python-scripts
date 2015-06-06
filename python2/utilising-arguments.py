#! /usr/bin/env python

import os, sys

def _skin_(arguments):
	print arguments
	arg = list(enumerate(arguments))
#	print arg
#	print len(arg)
	for i,j in arg:
		if j == '-h':
			print "usage: [-h : shows this message] \n       [[ -c : do a count] directory]"
		elif j == '-c':
			path = arguments[int(i)+1]
			print _getlistoffilesinpath(path)

def _getlistoffilesinpath(path):
	if os.path.exists(path) == True:
		print os.listdir(path)
		number_of_elements_in_path = len(os.listdir(path))
		return "There are %d files and directories in \'%s\'." % (number_of_elements_in_path, path)
	else:
		return "Path does not exists."

if __name__ == "__main__":
	arguments = sys.argv[1:]
	if arguments == []:
		print "usage: [-h : shows this message] \n       [[ -c : do a count] directory]"
	else:
		_skin_(arguments)