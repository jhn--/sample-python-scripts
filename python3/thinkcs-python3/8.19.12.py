'''
8.19.12
Write a function that removes the first occurrence of a string from another string:

test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
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

def remove(ph, w):
    l_ph = len(ph)
    l_w = len(w)
    i = 0
    w_in_list_form = []
    new_w_in_list_form = []
    new_w = ""
    if ph in w:
        for x in w:
            w_in_list_form.append(x)
            #print(w_in_list_form) #working
        while (i + l_ph) < (l_w + 1):
            if ph == w[i:i+l_ph]:
                del w_in_list_form[i:i+l_ph] #maybe I'm cheating; they might not want me to use the del keyword.
                new_w = ''.join(w_in_list_form)
                return new_w
            i += 1
    return w

#remove("an", "banana") == "bana"


test(remove("an", "banana") == "bana")
test(remove("cyc", "bicycle") == "bile")
test(remove("iss", "Mississippi") == "Missippi")
test(remove("eggs", "bicycle") == "bicycle")
