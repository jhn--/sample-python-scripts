#14.4

from unit_tester import test
import time

def text_to_words(the_text):
    my_substitutions = the_text.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\", "abcdefghijklmnopqrstuvwxyz                                          ")
    cleaned_text = the_text.translate(my_substitutions)
#    print(my_substitutions)
#    print(type(my_substitutions)) #<class 'dict'>
#    print("************************************************************")
#    print(cleaned_text)
#    print("============================================================")
    wds = cleaned_text.split()
    return wds

def get_words_in_the_book(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
#    print(result)
    return result

def merge_present_second_not_first(list1, list2):
    """ Another way of returning list of words in wds that do not occur in vocab """
    result = []
    l1i = 0
    l2i = 0
    while True:
        if list1[l1i] == list2[l2i]:
            l1i += 1
            l2i += 1
        elif list1[l1i] < list2[l2i]:
            l1i += 1
        else:
            result.append(list2[l2i])
            l2i += 1

        if l1i >= len(list1):
            result.extend(list2[l2i:])
            return result
        if l2i >= len(list2):
            return result

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub: # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

#        print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'".format(lb,ub , ub-lb, item_at_mid, target))

        if item_at_mid == target:
            return mid_index
        if item_at_mid < target:
            lb = mid_index + 1
        else:
            ub = mid_index

def remove_adjacent_dups(xs):
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e
    return result

xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]

#test(search_binary(xs, 20) == -1)
#test(search_binary(xs, 99) == -1)
#test(search_binary(xs, 1) == -1)

#for (i, v) in enumerate(xs):
#    test(search_binary(xs, v) == i)
#book_words = get_words_in_the_book("alice_in_wonderland.txt")
all_words = get_words_in_the_book("alice_in_wonderland.txt")
all_words.sort()
book_words = remove_adjacent_dups(all_words)

print("There are {0} words in the book. Only {1} are unique.".format(len(all_words), len(book_words)))
print("The first 100 words are\n{0}".format(book_words[:100]))

bigger_vocab = load_words_from_file("vocab.txt")
t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()

print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds".format(t1 - t0))

t2 = time.clock()
missing_words = merge_present_second_not_first(bigger_vocab, book_words)
t3 = time.clock()
print("find_unknown_words(): There are {0} unknown words.".format(len(missing_words)))
print("find_unknown_words(): That took {0:.4f} seconds".format(t3 - t2))

test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) == ["a", "big", "bite", "dog"])