#! /usr/bin/env python

varlogmsg = open('/var/log/messages', 'r')
csvfile = open('file.csv', 'w')

_time = []
_numberoftimes = {}

list_varlogmsg = varlogmsg.readlines()
for i in list_varlogmsg:
    a = i[:12]
    _time.append(a)

_time = sorted(_time)
print _time

for i in _time:
	count = _time.count(i)
	_numberoftimes[i] = count

for i in _numberoftimes:
	print i,", ", _numberoftimes[i], "\n"

csvfile.write('minute, number_of_messages\n')

for i in _numberoftimes:
	csvfile.write(i + ", " + str(_numberoftimes[i])+"\n")

varlogmsg.close()
csvfile.close()