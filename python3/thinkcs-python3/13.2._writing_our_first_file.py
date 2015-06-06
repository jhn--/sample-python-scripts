'''
13.2._writing_our_first_file
'''

myfile = open("myfile.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()