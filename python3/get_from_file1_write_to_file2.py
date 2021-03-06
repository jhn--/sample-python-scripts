#python3

import sys, os
import argparse
from time import strftime
import time
start_time = time.time()

def checkfiles(file1, file2):
    """Simple check on whether the files exists. file1 should exist, file2 should not. If file2 exists, we can choose to overwrite it, or exit."""

    files = [file1, file2]

    if os.path.isfile(files[0]) == False:
        sys.exit("File {0} does't exist.".format(files[0]))
    elif os.path.isfile(files[1]) == True:
        answer = input("File {0} exists, do you want to overwrite it? ".format(files[1]))
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return files
        else:
            sys.exit("Exiting...")
    else:
        return files

def getoccurencesfromfile(file1, file2, svctime):
    """If the service time(svctime), column 4, from file is greater than a certain amount, copy them out into file2."""

    files = checkfiles(file1, file2)

    file1_read = open(files[0], "r")
    file2_write = open(files[1], "w")

    getline = file1_read.readlines()
    for i in getline:
        if float(i.split()[3]) > svctime:
            file2_write.write(i)
    file2_write.close()
    file1_read.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="Name of the first file (absolute or relative path) you are checking against.")
    parser.add_argument("file2", help="Name of the second file (absolute or relative path) which will be populated with the results.")
    parser.add_argument("seconds", type=float, help="Amount of time, in seconds, which will be matched against the service time column, column 4, from file1.")
    args = parser.parse_args()
    #print("{0} --- {1} --- {2}".format(args.file1, args.file2, args.seconds))

    getoccurencesfromfile(args.file1, args.file2, args.seconds)
    print("--- %s seconds ---" % (time.time() - start_time))