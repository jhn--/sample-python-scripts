#!/opt/local/bin/python2.7


#bfc = raw_input("enter your flying circus name!")
#lenbfc = len(bfc)
#print lenbfc
#print len(bfc)

def the_flying_circus():
	bfc = raw_input("enter your flying circus name!")
	lenbfc = len(bfc)
#Start coding here!
        if lenbfc == 0:
		print "Please enter a name for your flying circus, it has only " + str(lenbfc) + " chars long."
        	return False
    	elif lenbfc < 5:
        	print bfc + " is small,  only " + str(lenbfc) + " chars long."
        	return False
    	elif lenbfc >= 5 and lenbfc <=10:
        	print bfc + " is medium,  only " + str(lenbfc) + " chars long."
        	return False
    	else:
        	print bfc + " is big, it has " + str(lenbfc) + "chars long!"
        	return True
