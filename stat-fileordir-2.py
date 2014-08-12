#!/usr/bin/env python

import os

path = raw_input("Enter a absolute path to a directory or a file.\
	E.g. \"/bin\" or \"/bin/chmod\". > ")

def statfile(path):
	if os.path.exists(path) == True:
		statefileinfo = os.stat(path)
		return statefileinfo
	else:
		return "The path, \"%s\", does not exist." % path

print statfile(path)