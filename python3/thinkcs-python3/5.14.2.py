'''You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.
'''

#! /usr/bin/env python

def dayofweekreturn(dayleft, daysgone):
    '''
    I'm trying to find a way to remove a large chunk of daysgone.
    They can be modulus by 7, the number of days in a week.
    and then the remaining days can be added to the day user left.
    '''
    numberofdayslessthanaweek = daysgone % 7
    print(numberofdayslessthanaweek)
    total = dayleft + numberofdayslessthanaweek
    print(total)
    if total >= 0 and total < 7:
        getday(total)
    else:
        getday((total % 7))

def getday(num):
    print("aye")
    listofdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for i, j in enumerate(listofdays):
        if i == num:
            print ("You will return on day", i, "of the week, which is a", j)

dayleft = int(input(
    '''
    Which day did you leave?
    0 = Sunday
    1 = Monday
    2 = Tuesday
    3 = Wednesday
    4 = Thursday
    5 = Friday
    6 = Saturday
    : '''))

daysgone = int(input(
    '''
    How many days are you away?
    '''))

dayofweekreturn(dayleft, daysgone)