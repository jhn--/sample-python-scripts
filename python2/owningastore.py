#!/usr/bin/python2.7

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}

for x in prices and stock:
	print x
	print "price : " + str(prices[x])
	print "stock : " + str(stock[x])

#total = []
total = 0

for x in prices and stock:
	total += (prices[x] * stock[x])
#	total.append(y)

print "total = " + str(total)	

#for x in total:
#	total[x] = total[x] + total[x+1]

#print x