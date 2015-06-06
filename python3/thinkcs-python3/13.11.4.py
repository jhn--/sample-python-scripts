'''
13.11.4
Write a program that undoes the numbering of the previous exercise: it should read a file with numbered lines and produce another file without line numbers.
'''

def add_line_number(infile, outfile):
    f = open(infile, "r")
    xs = f.readlines()

    g = open(outfile, "w")
    for i in xs:
        a = i[5:]
        g.write(a)
    g.close()
    f.close()

add_line_number("line_text.txt", "unline_text.txt")