'''
13.7._an_example
This script can be used for removing comments, good for removing distracting comments from apache.conf etc
'''

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        #text = text.decode('utf-8')
        if len(text) == 0:
            print("empty line encountered, moving on to next line.")
            break
        if text[0] == "#":
            print("comment encountered, omitting..")
            continue

        outfile.write(text)

    infile.close()
    outfile.close()

filter("test_apache", "new_apache")