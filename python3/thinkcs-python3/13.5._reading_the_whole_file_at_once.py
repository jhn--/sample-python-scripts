'''
13.5._reading_the_whole_file_at_once
'''
file = "text.txt"
f = open(file)
content = f.read()
f.close()

words = content.split()
print(words)
for i in words:
    print(i)
print("There are {0} words in the file \"{1}\".".format(len(words), file))