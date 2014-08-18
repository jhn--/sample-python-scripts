#! /usr/bin/env python

import os

def getcontents(here):
	listing = {}
	_files = []
	insidehere = os.listdir(here)

	for i in insidehere:
		if os.path.isfile(os.path.join(here, i)):
			_files.append(i)
			listing['.'] = _files
		elif os.path.isdir(os.path.join(here, i)):
			listing[i] = os.listdir(os.path.join(here, i))
	showcontents(listing)

def showcontents(listing):
	for i in listing:
		print i
		for j in listing[i]:
			print "|---", j

here = raw_input("Enter full path: ")

if os.path.exists(here):
	getcontents(here)
else:
	print "Folder doesn't exists."