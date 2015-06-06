'''
find() for strings
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

def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#test(find("Compsci", "p") == 3)
#test(find("Compsci", "C") == 0)
#test(find("Compsci", "i") == 6)
#test(find("Compsci", "x") == -1)
#test(find("banana", "a") == 1) #find only finds the first instance, and then exist.

def find2(strng, ch, start):
    """
    mandatory 3rd input, for specifying starting index
    """
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def find3(strng, ch, start=0):
    """
    optional 3rd input, for specifying starting index
    """    
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#test(find3("Compsci", "p") == 3)

def find4(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

ss = "Python strings have some interesting methods."
test(find4(ss, "s") == 7)
test(find4(ss, "s", 7) == 7)
test(find4(ss, "s", 8) == 13)
test(find4(ss, "s", 8, 13) == -1)
test(find4(ss, ".") == len(ss)-1)

#test(find2("banana", "a", 2) == 3) #start from 3 element, will return first character found after "banana"[2]

'''
string function, part of the builtin library in python.
'''
#found = "banana".find("a")
#print(found)
