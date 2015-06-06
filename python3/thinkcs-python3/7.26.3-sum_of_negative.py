'''
Sum up all the negative numbers in a list.
'''

listofneg = [-1, -2, -3.4, 4, -5, 6, -7, 8, -9]

def sum_of_negative(listofneg):
    total = 0
    for i in listofneg:
        if i < 0:
            total += i
    return total

print(sum_of_negative(listofneg))