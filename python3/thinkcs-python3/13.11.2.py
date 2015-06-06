'''
13.11.2
Write a program that reads a file and prints only those lines that contain the substring snake.
'''

def find_word(file):

    word = "snake"

    f = open(file, "r")
    xs = f.readlines()
    f.close()

    print(xs)
    '''
    for i in xs:
        print(i)
    '''
    print("###################")
    for i in xs:
        if word in i:
            print(i)

find_word("text.txt")