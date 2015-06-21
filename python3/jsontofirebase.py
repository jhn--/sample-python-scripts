import requests
import argparse
from firebase import firebase

def getjson(jsonurl):
    """Get the json file from the URL."""
    req = requests.get(jsonurl)
    return req

def postfirebase(firebaseurl, jsondata, branch = ''):
    """Put the json information to firebase."""
    posttofirebase = firebase.FirebaseApplication(firebaseurl, None)
    if branch == '':
        posttofirebase.post('/', jsondata)
    else:
        branch = "/" + branch[0]
        posttofirebase.post(branch, jsondata)

def engine(jsonurl, firebaseurl, branch = ''):
    gotjson = getjson(jsonurl)
    gotjson = gotjson.json()
    postfirebase(firebaseurl, gotjson, branch)

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("jsonurl", help="Enter a url of a json file to import it into your firebase. E.g. https://test.example.org/example.json")
    parse.add_argument("firebaseurl", help = "Enter the url of your firebase account. E.g. https://test.firebaseio.com")
    parse.add_argument("--branch", nargs = 1, help = "Optional: Enter the name of the branch you want to create for this set of json data in firebase.")
    args = parse.parse_args()
    print(args)
    if args.branch is None:
        engine(args.jsonurl, args.firebaseurl)
    else:
        engine(args.jsonurl, args.firebaseurl, args.branch)

if __name__ == '__main__':
    main()