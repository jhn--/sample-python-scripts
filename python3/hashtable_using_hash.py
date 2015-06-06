dict = {}

def multi_insert(many_items):
    for i in many_items:
        a = hashtable(i)
    return a

def hashtable(entry):
    beta = hash(entry)
    dict[beta] = entry
    return dict

def get_element(target, dict = dict):
    beta = hash(target)
    try:
        result = dict[beta]
        return "\'{0}\' can be found at index \'{1}\'".format(target, beta)
    except Exception:
    #except KeyError:
        return "\'{0}\' does not exist.".format(target)

print(multi_insert(['hoe chih chang', 'happy happy', 'are you okay?', 'lim bo seng', 'ong teng cheong']))
print(get_element('hoe chih chang'))
print(get_element('john hoe'))