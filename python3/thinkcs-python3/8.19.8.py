'''
8.19.8
Write a function that mirrors its argument:

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")
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

def mirror(s):
    reverse_s = reverse(s)
    mirror_s = s+reverse_s
    return mirror_s

def reverse(s):
    """Use the built-in function reversed() to reverse the elements."""
    word = ""
    for i in reversed(s):
        word += i
    return word

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")