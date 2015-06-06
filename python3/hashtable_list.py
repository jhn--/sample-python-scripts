"""Populating a list via folding method, the length of the list is not predefined. Usually it should be a database table involved, but for now lets just create a list."""

list = []

def multi_insert(many_items, list = list):
    for i in many_items:
        a = hash_by_folding(i, list)
    return a

def hash_by_folding(entry, list):
    #Let us assume that the variable, "entry", for this program's context, are names.
    prime = 11
    if len(list) == 0:
        for i in range(prime):
            list.append(None)
    else:
        pass
    new_entry = entry.replace(" ", "")
    alpha = 0
    for i in new_entry:
        alpha += ord(i)
    beta = alpha % prime
    if list[beta] == None:
        list[beta] = entry
    else:
        print("Collision! Index {0} has been already been populated by {1} and cannot be overwritten by {2}".format(beta, list[beta], entry))
    print("{0}, {1}".format(beta, entry))
    return list

#print(hash_by_folding("hoe chih chang"))
print(multi_insert(['hoe chih chang', 'happy happy', 'are you okay?', 'lim bo seng', 'ong teng cheong']))
#print(list)