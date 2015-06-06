'''
8.19.11
Write a function that counts how many times a substring occurs in a string:

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)
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

def count(ph, w):
    #slept through the night dreaming about this problem but now i managed to solve it, glad.
    """take a portion of the word; with length equivalent to the length of the search phrase, and compare them. """
    l_ph = len(ph)
    l_w = len(w)
    i = 0
    count = 0
    #while i < (l_w + 1) and (i + l_ph) < (l_w + 1): 
    # "i" starts from 0 and will always be lesser than l_w + 1, do not need this clause.
    while (i + l_ph) < (l_w + 1):
        if ph == w[i:i+l_ph]:
            count += 1
        i += 1
    return count

test(count("is", "Mississippi") == 2)
test(count("an", "banana") == 2)
test(count("ana", "banana") == 2)
test(count("nana", "banana") == 1)
test(count("nanan", "banana") == 0)
test(count("aaa", "aaaaaa") == 4)

'''
def count(ph, w):
    """Use str.count() built-in method"""
    import string
    return str.count(w, ph)
'''
'''
def count(ph, w):
    """My own ingenious, but unsuitable method."""
    new_w = ""
    if ph in w:
        w_minus_ph = (w.split(ph))
        for i in w_minus_ph:
            new_w += i
        diff = len(w) - len(new_w)
        count = int(diff / len(ph))
    else:
        return 0
    return count
'''
'''
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
'''