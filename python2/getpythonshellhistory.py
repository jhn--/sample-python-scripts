#! /usr/bin/env python

import os, readline

print os.getcwd()

f = open(os.path.join(os.getcwd(), 'python-command-history.txt'), 'w')
#with open(os.path.join(os.getcwd(), 'python-command-history.txt'), 'w') as f:
try:
	for i in range(readline.get_current_history_length()):
		f.write(str(readline.get_history_item(i))+"\n")
except IOError as (errno, strerror):
	print errno +": "+strerror
finally:
	f.close()