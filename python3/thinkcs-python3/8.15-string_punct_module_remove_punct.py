'''
removing punctuations using the string module.
'''

import string, sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno     # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

test(remove_punctuation('"Well, I never did!", said Alice.') ==
                            "Well I never did said Alice")
test(remove_punctuation("Are you very, very, sure?") ==
                             "Are you very very sure")