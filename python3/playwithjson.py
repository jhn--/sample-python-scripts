#/Users/john/.nix-profile/bin/python3.4

import os
import argparse
import json
from pprint import pprint
import sys

class playwithjson:
    """A simple class which opens and reads json files, there's an sample json file to use @ /Users/john/Dropbox/Work/projects/programming/python/sample-python-scripts/example.json"""
    def __init__(self, jsonfile):
        self.jsonfile = jsonfile
        print("##1")
        print(self.jsonfile)
        print("##2")
        print(type(self.jsonfile))
        print("##3")

    def __str__(self):
        print(self.jsonfile)

    def access_json(self):
        print("##4")
        print(str(self.jsonfile))
        print("##5")
        print(str(self.jsonfile).endswith('.json'))
        print("##6")
        if str(self.jsonfile).endswith('.json'):
            try:
                fp = open(self.jsonfile, "r+")
            except IOError as e:
                if e.errno == errno.EACCES:
                    raise e.errno
                    exit()
            else:
                with fp:
                    #print(fp.read())
                    #print(type(fp.read()))
                    #return fp.read()
                    jp = json.load(fp)
                    #print(jp)
                    print(type(jp))
                    return jp
        else:
            print("This file is a not a json file.")

    def showjsoncontents(self):
        jp = self.access_json()
        for i in jp:
            pprint(i)
#            pprint(i)
            #return i
#        for index in jp:
#            return index
#            for k, v in index.items():
#                return k, v

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonfile", help="Absolute path of the file. E.g. /path/to/file")
    args = parser.parse_args()

    right = playwithjson(args.jsonfile)
    right.__str__()
    #print(right)
    right.showjsoncontents()