'''
8.19.10
Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
# test(is_palindrome(""))    # Is an empty string a palindrome?
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

def is_palindrome(s):
    if s == reverse(s):
        return True
    return False

def reverse(s):
    """My own method of reversing."""
    reverse_s = []
    word = ""
    for i in range(0, len(s)):
        reverse_s.insert(-i, s[i])
        #print(-i, s[i])
    #print(reverse_s)
    for i in reverse_s:
        word += i
    #print(word)
    return word

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
# test(is_palindrome(""))    # Is an empty string a palindrome?