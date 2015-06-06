'''
remove vowels
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


def remove_vowels(s):
    '''
    #compare each character in word with the list of vowels
    #do not need zip(), both entities are strings.
    '''
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels

'''
#############################################################################if i not know the "in" keyword, i'll probably be writing the remove_vowels() function like below.
And fail miserably. The code below doesn't work.
'''
#def remove_vowels(s):
#    vowels = "aeiouAEIOU"
#    s_sans_vowels = ""
#    for x in s:
#        for v in vowels:
#            if x == v:
#                for c in s_sans_vowels:
#                    if x == c:
#                        continue
#                s_sans_vowels += x
#    print(s_sans_vowels)
#    return s_sans_vowels
'''
#############################################################################
'''

test(remove_vowels("compsci") == "cmpsc")
test(remove_vowels("aAbEefIijOopUus") == "bfjps")