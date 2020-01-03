import os
#from html.parser import HTMLParser
#import HTMLParser
import json, argparse
from firebase import firebase

class bookmarkparser:
    my_keys = ''
    my_values = ''
    my_dict = {}
    '''
    def reset(self):
        HTMLParser.reset(self)
        self.a = False
    '''
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs[0][0] == 'href':
            self.a = True
            #self.my_keys = str(attrs[0][1].strip()).replace('\n', '').replace('.', '').replace('$', '').replace('#', '').replace('[', '').replace(']', '').replace('/', '')
            self.my_keys = str(attrs[0][1].strip()).replace('\n', '')

    def handle_data(self, data):
        if self.a == True:
            #self.my_values = str(data.strip()).replace('\n', '').replace('.', '').replace('$', '').replace('#', '').replace('[', '').replace(']', '').replace('/', '')
            self.my_values = str(data.strip()).replace('\n', '')

    def handle_endtag(self, tag):
        if tag == 'a':
            self.my_dict[self.my_values] = self.my_keys 
            self.a = False

    def openbookmark(self, bookmark):
        try:
            with open(bookmark, 'r') as op:
                opread = str(op.read())
                return opread
                opread.close()
        except Exception as e:
            raise e 

    def dumpjson(self, jsonpath, value):
        with open(jsonpath, 'w') as writetojson:
            json.dump(value, writetojson)
        writetojson.close()

    def uploadtofirebase(self, firebaseurl, jsonpath):
        firebased = firebase.FirebaseApplication(firebaseurl, None)
        with open(jsonpath, 'r') as jsonfp:
            jp = json.load(jsonfp)
        #    print(jp)
            firebased.post('/bookmarks', jp)
            jsonfp.close()

if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser(description = "Parse bookmark and load them into firebase or a json file.")
    arg_parse.add_argument('file', help='absolute path to the bookmark file.')
    arg_parse.add_argument('-f', '--firebase', nargs = 1, help = 'Enter the URL of firebase URL. E.g. https://example.firebaseio.com')
    arg_parse.add_argument('-j', '--json', nargs = 1, help = 'Enter the absolute path of the json file')
    args = arg_parse.parse_args()



'''    
    parser = bookmarkparser()
    parser.feed(openbookmark('/Users/john/Dropbox/bookmarks_8_8_15.html'))
    dumpjson(parser.my_dict)
    #uploadtofirebase()
'''