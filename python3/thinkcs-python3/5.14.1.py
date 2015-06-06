'''
Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).
'''

#! /usr/bin/env python

def numtoday(num, listofdays):
#    print(num)
    if num >= 0 and num < 7:
        if num == 0:
            print(listofdays[0])
        elif num == 1:
            print(listofdays[1])
        elif num == 2:
            print(listofdays[2])
        elif num == 3:
            print(listofdays[3])
        elif num == 4:
            print(listofdays[4])
        elif num == 5:
            print(listofdays[5])
        else:
            print(listofdays[6])
    else:
        print("Number", num, "is out of range.")
        return

def another_numtoday(num, listofdays):
#    num = int(num)
#    print(num)
    if num >= 0 and num < 7:
        for i, j in enumerate(listofdays):
            if i == num:
                print("its ", j)
    else:
        print("Number", num, "is out of range.")
        return

def checkingforint():
    num = input(
        '''
        Enter an integer between 0 to 6.
        (Decimals are okay, I'll convert it into integer.)
        : ''')
    listofdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    try:
        int_num = int(float(num))
        numtoday(int_num, listofdays)
        another_numtoday(int_num, listofdays)
    except:
        print("Error, you did not enter a number.")

checkingforint()