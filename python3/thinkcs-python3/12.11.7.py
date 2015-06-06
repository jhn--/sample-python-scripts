'''
12.11.7
'''

import unit_tester

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    return new.join(s.split(old))


unit_tester.test(myreplace(",", ";", "this, that, and some other thing") ==
                         "this; that; and some other thing")
unit_tester.test(myreplace(" ", "**",
                 "Words will now be separated by stars.") ==
                 "Words**will**now**be**separated**by**stars.")