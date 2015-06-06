'''
Write a function, is_prime, which takes a single integer argument and returns True when the argument is a prime number and False otherwise. Add tests for cases like this:

test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))
The last case could represent your birth date. Were you born on a prime day? In a class of 100 students, how many do you think would have prime birth dates?
'''
'''
what makes a number a prime number?
1. positive integer
2. not 0
3. not 1
4. can only divded by 1
5. can only be divided by itself
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

def is_prime(n):
    '''
    using trial division
    '''
    if n <= 3:                                  #(negative to 3)
        if n <= 1:                              #(negative to 1)
            return False
        return True                             #removed all negative numbers, 0 and 1. 2 and 3 remains and are prime numbers
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True

test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))
test(is_prime(19810505))