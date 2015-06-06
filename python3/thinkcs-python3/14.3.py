from unit_tester import test

def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
#    print(result)
    return result

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

vocab = ["apple", "boy", "dog", "down", "fell", "girl", "grass", "the", "tree"]
#used split to create our list of words - it is easier than typing out the list, and very convenient if you want to input a sentence into the program and turn it into a list of words.
book_words = "the apple fell from the tree to the grass".split()

test(find_unknown_words(vocab, book_words) == ["from", "to"])
test(find_unknown_words([], book_words) == book_words)
test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])