'''
13.11.1
Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file.)
'''

oldfile = "text.txt"
newfile = "rev_text.txt"

def reverse_file(old, new):
    f = open(old, "r")
    xs = f.readlines()
    f.close()

    g = open(new, "w")
    for i in range(len(xs)-1, 0, -1):
        g.write(xs[i])
    g.close()

'''
def reverse_file(old,new):
    f = open(old)
    content = f.read()
    f.close()

    g = open(new, "w")
    content = content.split()
    print(content)
    for i in range(len(content)-1, 0, -1):
        g.write(content[i])
    g.close()
'''

reverse_file(oldfile, newfile)