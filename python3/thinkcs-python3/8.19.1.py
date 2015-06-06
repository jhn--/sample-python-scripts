'''
8.19.1
What is the result of each of the following:

>>> "Python"[1]
>>> "Strings are sequences of characters."[5]
>>> len("wonderful")
>>> "Mystery"[:4]
>>> "p" in "Pineapple"
>>> "apple" in "Pineapple"
>>> "pear" not in "Pineapple"
>>> "apple" > "pineapple"
>>> "pineapple" < "Peach"
'''

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno     # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(("Python"[1]) == "y")
test(("Strings are sequences of characters."[5]) == "g")
test((len("wonderful")) == 9)
test(("Mystery"[:4]) == "Myst")
test(("p" in "Pineapple") == True) #case insensitive
test(("apple" in "Pineapple") == True)
test(("pear" not in "Pineapple") == True)
test(("apple" > "pineapple") == False)
test(("pineapple" < "Peach") == False)