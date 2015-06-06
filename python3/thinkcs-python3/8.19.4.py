'''
http://openbookproject.net/thinkcs/python/english3e/strings.html
8.19.4
Now rewrite the count_letters function so that instead of traversing the string, it repeatedly calls the find method, with the optional third parameter to locate new occurrences of the letter being counted.
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

def count_letters(strng, ch, start=0):
    location = []
    count = 0
    while start != -1:
        start = find(strng, ch, start)
        if start != -1:
            location.append(start)
            start += 1
            count += 1
    return "There are {0} instances of \'{1}'\' and they can be found in {2}. ".format(count, ch, location)


def find(strng, ch, start=0):
    """
    optional 3rd input, for specifying starting index
    """    
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#print(count_letters("banana", "a"))
print(count_letters("0123567810", "a"))


'''
having problems finding a way to have a flow control variable in count_letters() to accept ix from find(), this controling variable also will end all when it recieves a -1 from find() but its solved. looking for better approach.
'''