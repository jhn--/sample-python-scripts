'''
13.8._directories
'''
"""basic script based on section 13.8 of "http://openbookproject.net/thinkcs/python/english3e/files.html". There are alot more can do here. eg. import os module and allow user input to read files, like the "cat" command."""

wordsfile = open("/usr/share/dict/words", "r")
wordlist = wordsfile.readlines()
print(wordlist[:6])