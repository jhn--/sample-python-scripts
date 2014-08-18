#! /usr/bin/env python

import os

listing = {}
_files = []

here = os.getcwd()
insidehere = os.listdir(os.getcwd())

for i in insidehere:
	if os.path.isfile(i):
		_files.append(i)
		listing['.'] = _files
	elif os.path.isdir(i):
		listing[i] = os.listdir(os.path.join(here, i))

for z in listing:
	print z
	for y in listing[z]:
		print "|--", y