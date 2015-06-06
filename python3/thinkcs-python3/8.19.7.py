'''
8.19.7
Write a function that reverses its string argument, and satisfies these tests:

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")
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

def reverse(s):
    """My own method of reversing."""
    reverse_s = []
    word = ""
    for i in range(0, len(s)):
        reverse_s.insert(-i, s[i])
        print(-i, s[i])
    #print(reverse_s)
    for i in reverse_s:
        word += i
    #print(word)
    return word

'''
def reverse(s):
    """Use the built-in function reversed() to reverse the elements."""
    word = ""
    for i in reversed(s):
        word += i
    return word
'''

test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "a")