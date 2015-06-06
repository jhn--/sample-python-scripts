#lets just try to open a file first.

import sys, os

here = os.getcwd()

there_file = '/Users/john/Documents/SwiftServe/FETCH_WIDXMEM_20150424.txt'
there_file2 = '/Users/john/Documents/SwiftServe/WASD.txt'

def getonelinefromfile(there_file):
    there_file_contents = open(there_file, 'r')
    there_file2_write = open(there_file2, 'w')
    getline = there_file_contents.readlines()
    for i in getline:
        if float(i.split()[3]) > 1:
            there_file2_write.write(i)
    there_file2_write.close()
    there_file_contents.close()

try:
    print(getonelinefromfile(there_file))
except Exception as e:
    raise e

print(here) 