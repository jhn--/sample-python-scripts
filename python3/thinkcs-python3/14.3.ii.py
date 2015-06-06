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

def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

test(text_to_words("My name is Earl") == ["my", "name", "is", "earl"])
test(text_to_words('"Well, I never!", said Alice.') == ["well", "i", "never", "said", "alice"])

book_words = get_words_in_the_book("alice_in_wonderland.txt")
print("There are {0} words in the book, the first 100 words are\n {1}".format(len(book_words), book_words[:100]))

bigger_vocab = load_words_from_file("vocab.txt")
t0 = time.clock()
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.clock()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds".format(t1 - t0))
#print("There are {0} missing words, which are\n {1}".format(len(missing_words), missing_words))