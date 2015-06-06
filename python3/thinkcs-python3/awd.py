'''
8.19.5
Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”. Your program should print an analysis of the text like this:

Your text contains 243 words, of which 109 (44.8%) contain an "e".
'''

import string

def countwords_w_e(s):
    """Removes punctuation in sentence and pass new sentence into count_words()."""
    s_wo_punctuation = ""
    for i in s:
        if i == "-":
            i = " "
        if i not in string.punctuation:
            s_wo_punctuation += i
    listofwords = count_words(s_wo_punctuation)

def count_words(s):
    """Takes sentence from countwords_w_e(), count the number of words in sentence, pass sentence to count_num_of_e() to count words with the letter "e" inside. All results then pass to return_analysis() for printing."""
    listofwords = []
    num_of_e = []
    listofwords = s.split()
    num_of_e = count_num_of_e(listofwords)
    return_analysis(len(listofwords), num_of_e)

def count_num_of_e(s):
    """Takes sentence from count_words(), count number of words with "e" within, calculates percentage. Insert results into a list call answer, then returns back to count_words()."""
    count = 0
    answer = []
    for i in s:
        if "e" in i:
            count += 1
    percentage = (count / len(s)) * 100
    answer.append(count)
    answer.append(percentage)
    return answer

def return_analysis(x, y):
    """Takes answer[] from count_words() and prints them."""
    print("Your text contains {0} words, of which {1} ({2:.1f}%) contain an \"e\".".format(x, y[0], y[1]))

sentence = '''
Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
'''

countwords_w_e(sentence)