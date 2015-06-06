'''
Count how many words in a list have length 5.
'''

listofwords = ["happy", "win", "lose", "rojak", "lovely"]

def words_length_5(listofwords):
    total = 0
    for i in listofwords:
        if len(i) == 5:
            total += 1
    return total

print(words_length_5(listofwords))