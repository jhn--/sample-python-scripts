'''
13.9._fetching_something_from_the_web_and_printing_it_STDOUT
'''
"""
Another great start to what can be a tool to help download a number of files automatically, now all i need is to write another script to parse hyperlinks.
Ought to include "try" functionalities. And some verbose messages.
"""

import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta

contents = retrieve_page("http://www.ietf.org/rfc/rfc1918.txt")
for i in contents.split("\n"):
    print(i)