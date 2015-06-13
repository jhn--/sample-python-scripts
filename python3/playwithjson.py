#/Users/john/.nix-profile/bin/python3.4

import os
import argparse
import json
from pprint import pprint
import sys

class playwithjson:
    """A simple class which opens and reads json files."""
    def __init__(self, jsonfile):
        self.jsonfile = jsonfile

    #def __str__(self):
    #    print(self.jsonfile)

    def access_json(self):
        if str(self.jsonfile).endswith('.json'):
            try:
                fp = open(self.jsonfile, "r+")
            except IOError as e:
                if e.errno == errno.EACCES:
                    raise e.errno
                    exit()
            else:
                with fp:
                    jp = json.load(fp)
                    return jp
                    fp.close()
        else:
            print("This file is a not a json file.")

    def showjsoncontents(self):
        jp = self.access_json()
        for i in jp:
            pprint(i)

    def getjsonkeys(self):
        keys = []
        jp = self.access_json()
        for k, v in jp[0].items():
            keys.append(k)
        print("The keys of this json file is: ")
        for i in keys:
            print(i)

    def getjsonkeyinfo(self, key):
        jp = self.access_json()
        key_values = []
        for i in jp:
            key_values.append(i[key])
        print(key_values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonfile", help="Absolute path of the file. E.g. /path/to/file")
    args = parser.parse_args()

    right = playwithjson(args.jsonfile)
    #right.showjsoncontents()
    right.getjsonkeys()
    right.getjsonkeyinfo("name")