'''
12.11.8
wordtools.py
'''

import unit_tester

def cleanword(a):
    import string
    for i in a:
        if i in string.punctuation:
            a = "".join(a.split(i))
    #print (a)
    return a

def has_dashdash(a):
    if "-" in a:
        return True
    return False

def extract_words(a):
    import string
    for i in a:
        if i in string.punctuation:
            a = " ".join(a.split(i))
    a = a.lower()
#    print(a.split())
    return a.split()

def wordcount(a, b):
    count = 0
    for i in b:
        if i in a:
            count += 1
    return count

def wordset(a):
    yeah = []
    for i in a:
        if i not in yeah:
            yeah.append(i)
        pass
    yeah.sort()
    return yeah

def longestword(a):
    count = 0
    for i in a:
        if len(i) > count:
            count = len(i)
    return count

unit_tester.test(cleanword("what?") == "what")
unit_tester.test(cleanword("'now!'") == "now")
unit_tester.test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

unit_tester.test(has_dashdash("distance--but"))
unit_tester.test(not has_dashdash("several"))
unit_tester.test(has_dashdash("spoke--"))
unit_tester.test(has_dashdash("distance--but"))
unit_tester.test(not has_dashdash("-yo-yo-"))

unit_tester.test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
unit_tester.test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

unit_tester.test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
unit_tester.test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
unit_tester.test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
unit_tester.test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

unit_tester.test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
unit_tester.test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
unit_tester.test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

unit_tester.test(longestword(["a", "apple", "pear", "grape"]) == 5)
unit_tester.test(longestword(["a", "am", "I", "be"]) == 2)
unit_tester.test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
unit_tester.test(longestword([ ]) == 0)
