'''
8.19.3

Encapsulate

fruit = "banana"
count = 0
for char in fruit:
    if char == "a":
        count += 1
print(count)
in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments. Make the function return the number of characters, rather than print the answer. The caller should do the printing.
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

def count_letters(w, ch):
    count = 0
    for char in w:
        if char == ch:
            count += 1
    return count

test(count_letters("banana", "a") == 3)
test(count_letters("banana", "n") == 2)
test(count_letters("python", "n") == 1)