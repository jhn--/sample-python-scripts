'''
13.9._what_about_fetching_something_from_the_web
'''
"""
Another great start to what can be a tool to help download a number of files automatically, now all i need is to write another script to parse hyperlinks.
Ought to include "try" functionalities. And some verbose messages.
"""

import urllib.request

url = "http://www.ietf.org/rfc/rfc793.txt"
destinationfile = "rfc793.txt"

urllib.request.urlretrieve(url, destinationfile)