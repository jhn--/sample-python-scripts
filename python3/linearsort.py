def linearsearch(input, value):
    """Now, this is better, I've figured it out."""
    count = 0
    for i in input:
        if (value == i):
            count += 1
    if count > 0:
        return "Value, {0}, is in the list".format(value)
    else:
        return "Value, {0}, cannot be found".format(value)

'''
def linearsearch(input, value):
    """I really doubt this is linear search. I am basically not doing a search. =( """
    if value in input:
        return "Value, {0}, is in the list".format(value)
    else:
        return "Value, {0}, cannot be found".format(value)
'''

print(linearsearch([1,2,3,4,5,6], 5))

print(linearsearch([1,2,3,4,5,6], 10))