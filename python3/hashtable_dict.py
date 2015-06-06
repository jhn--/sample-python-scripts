dict = {}
prime = 11 #Maybe I can use random? hmmm

def multi_insert(many_items, dict = dict, prime = prime):
    for i in many_items:
        a = hashtable(i, prime)
    return a

def hashtable(entry, prime = prime):
    new_entry = entry.replace(" ", "")
    alpha = 0
    for i in new_entry:
        alpha += ord(i)
    beta = alpha % prime
    dict[beta] = entry
    return dict

print(multi_insert(['hoe chih chang', 'happy happy', 'are you okay?', 'lim bo seng', 'ong teng cheong']))

def get_element(target, dict = dict):
    new_target = target.replace(" ","")
    alpha = 0
    for i in new_target:
        alpha += ord(i)
    beta = alpha % prime
    try:
        result = dict[beta]
        return "\'{0}\' can be found at index \'{1}\'".format(target, beta)
    except Exception:
    #except KeyError:
        return "\'{0}\' does not exist.".format(target)

print(get_element('hoe chih chang'))
print(get_element('john hoe'))