'''
Sum up all the even numbers in a list.
'''

listofnum = [1,2,3,4,5,6,7,8,9]

def sum_of_even(listofnum):
    total = 0
    for i in listofnum:
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(listofnum))