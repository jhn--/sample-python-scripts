'''
8.19.13
Write a function that removes all occurrences of a string from another string:

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")
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


def remove_all(ph, w):
    if ph in w:
        new_w = ""
        new_w_list = []
        if ph in w:
            new_w_list = w.split(ph)
            #print(new_w_list)
        new_w = ''.join(new_w_list)
        #print(new_w)
        return new_w
    return w

'''
def remove_all(ph, w):
    l_ph = len(ph)
    l_w = len(w)
    w_list = []
    for i in w:
        w_list.append(i)
    i = 0
    if ph in w:
        while (i + l_ph) < (l_w + 1):
            if ph == w[i:i+l_ph]:
                del w_list[i:i+l_ph]
                new_w = ''.join(w_list)
                print(new_w)
            i += 1
        remove_all(ph, new_w)
    print(w)
    return w
'''

test(remove_all("an", "banana") == "ba")
test(remove_all("cyc", "bicycle") == "bile")
test(remove_all("iss", "Mississippi") == "Mippi")
test(remove_all("eggs", "bicycle") == "bicycle")