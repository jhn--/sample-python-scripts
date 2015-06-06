#!/opt/local/bin/python2.7
"""
s=raw_input("do you want to shutdown?")

def shut_down(s):
	if s == "yes" or s =="Yes" or s =="YES":
		print "Shutting down..."
	elif s == "no" or s == "No" or s == "NO":
		print "Shutdown aborted!"
	else:
		print "Sorry, I didn't understand you."

shut_down(s)
"""
s=raw_input("do you want to shutdown?")

def shut_down(s):
	if s.lower() == "yes":
		return "'Shutting down...'"
	elif s.lower() == "no":
		return "'Shutdown aborted!'"
	else:
		return "'Sorry, I didn't understand you.'"

shut_down(s)