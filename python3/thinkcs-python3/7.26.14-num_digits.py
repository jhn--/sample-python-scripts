'''
What will num_digits(0) return? Modify it to return 1 for this case. Why does a call to num_digits(-24) result in an infinite loop? (hint: -1//10 evaluates to -1) Modify num_digits so that it works correctly with any integer value. Add these tests:

test(num_digits(0) == 1)
test(num_digits(-12345) == 5)
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

def num_digits(n):
    n = int(abs(n))
    count = 0
    if n == 0:
        return 1
    else:
        while n != 0:
            n //= 10
            count += 1
        return count

test(num_digits(0) == 1)
test(num_digits(-12345) == 5)