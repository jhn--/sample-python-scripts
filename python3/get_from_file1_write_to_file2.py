#python3

import sys, os
from optparse import OptionParser
from time import strftime

def checkfiles(file1, file2):
    """Simple check on whether the files exists. file1 should exist, file2 should not."""

    files = [file1, file2]
    try:
        os.stat(file1)
    except OSError as (errno, strerror):
        return "OS Error: Error code %d. The file/directory: \"%s\". %s." % (errno, os.path.basename(file1), strerror)

    try:
        os.stat(file2)
        answer = input("File {0} exists, do you want to overwrite it?")
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return files
        else:
            print("Exiting..")
            return
    except:
        return files

def getoccurencesfromfile(file1, file2, svctime):
    """If the service time(svctime), column 4, from file is greater than a certain amount, copy them out into file2."""

    files = checkfiles(file1, file2)
    file1_read = os.open(files[0], 'r')
    file2_write = os.open(files[1], 'w')

    getline = file1_read.readlines()
    for i in getline:
        if float(i.split()[3]) > svctime:
            file2_write.write(i)
    file2_write.close()
    file1_read.close()

#def changefilename(file2):
#    datum = strftime("%Y-%m-%d_%H:%M:%S") #E.g. '2015-06-06_23:14:17'
#    file2a = os.path.split(file2)[0] #E.g. '('/path/to', 'file.ext')' or ('', 'file.ext')
#    file2b = os.path.split(file2)[1]

if __name__ == '__main__':
    getoccurencesfromfile(*args)