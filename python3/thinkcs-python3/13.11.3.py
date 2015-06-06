'''
13.11.3
Write a program that reads a text file and produces an output file which is a copy of the file, except the first five columns of each line contain a four digit line number, followed by a space. Start numbering the first line in the output file at 1. Ensure that every line number is formatted to the same width in the output file. Use one of your Python programs as test data for this exercise: your output should be a printed and numbered listing of the Python program.
'''

def add_line_number(infile, outfile):
    f = open(infile, "r")
    xs = f.readlines()

    g = open(outfile, "w")
    for i, val in enumerate(xs):
        a = "{0:<5}{1}".format(i+1, val)
        g.write(a)
    g.close()
    f.close()

add_line_number("text.txt", "line_text.txt")