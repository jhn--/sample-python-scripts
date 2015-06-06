'''
Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
'''

def checkforsam(l):
    for i in l:
        if i == "sam":
            return uptoinclsam(l)
    return None                         #No "sam" found.

def uptoinclsam(l):
    total = 0
    for i in l:
        if i == "sam":
            total += 1
            break
        total += 1
    return total

listofwords = ["hello", "roar", "sam", "whew"]
listofwords2 = ["hello", "roar", "whew"]
listofwords3 = [ "sam", "hello", "roar", "whew"]

print(checkforsam(listofwords))
print(checkforsam(listofwords2))
print(checkforsam(listofwords3))