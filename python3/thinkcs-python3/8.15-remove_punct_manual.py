'''
removing of punctuation using self-defined punctuation string
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

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    new_word = ""
    for i in s:
        if i not in punctuation:
            new_word += i
    return new_word

test(remove_punctuation('"Well, I never did!", said Alice.') ==
                            "Well I never did said Alice")
test(remove_punctuation("Are you very, very, sure?") ==
                             "Are you very very sure")

my_story = '''
Pythons are constrictors, which means that they will 'squeeze' the life
out of their prey. They coil themselves around their prey and with
each breath the creature takes the snake will squeeze a little tighter
until they stop breathing completely. Once the heart stops the prey
is swallowed whole. The entire animal is digested in the snake's
stomach except for fur or feathers. What do you think happens to the fur,
feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
you guessed it --- snake POOP! '''

wds = remove_punctuation(my_story).split()
print(wds)