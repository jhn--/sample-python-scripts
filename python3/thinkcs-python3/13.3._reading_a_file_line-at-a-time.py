'''
13.3._reading_a_file_line-at-a-time
'''

mynewhandle = open("text.txt","r")

while True:                                     #keep reading forever
    theline = mynewhandle.readline()            #try to read next line
    if len(theline) == 0:                       #if there are no more lines, 
        break                                   #   leave the loop
        #The break statement, like in C, breaks out of the smallest enclosing for or while loop, unlike "return".
    
    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()