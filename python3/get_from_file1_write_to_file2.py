#python3

import sys, os
import argparse
from time import strftime

def checkfiles(file1, file2):
    """Simple check on whether the files exists. file1 should exist, file2 should not."""

    files = [file1, file2]
    try:
        os.stat(files[0])
    except OSError as (errno, strerror):
        return "OS Error: Error code %d. The file/directory: \"%s\". %s." % (errno, os.path.basename(files[0]), strerror)

    try:
        os.stat(files[1])
        answer = input("File {0} exists, do you want to overwrite it? ".format(files[1]))
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
    
    print(files)
    print(files[0])
    print(type(files[0]))
    print(files[1])
    print(type(files[1]))

    file1_read = os.open(files[0], "r")
    file2_write = os.open(files[1], "w")

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
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="Name of the first file (absolute or relative path) you are checking against.")
    parser.add_argument("file2", help="Name of the second file (absolute or relative path) which will be populated with the results.")
    parser.add_argument("seconds", type=float, help="Amount of time, in seconds, which will be matched against the service time column, column 4, from file1.")
    args = parser.parse_args()
    getoccurencesfromfile(args.file1, args.file2, args.seconds)