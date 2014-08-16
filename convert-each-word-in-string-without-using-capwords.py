#! /usr/bin/env python

import string

sentence = raw_input("Enter a sentence: ")

def converting(sentence):
    sentence = sentence.split()
    sentence2 = []
    for i in sentence:
        sentence2.append(string.capitalize(i))
    sentence3 = " ".join(sentence2)
    print sentence3

if __name__ == "__main__":
    converting(sentence)
