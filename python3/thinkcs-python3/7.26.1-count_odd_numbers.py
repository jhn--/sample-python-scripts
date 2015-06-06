'''
Write a function to count how many odd numbers are in a list.
'''

listofnum = [1,2,3,4,5,6,7,8,9]

def count_odd(listofnum):
    count = 0
    for i in listofnum:
        if i % 2 != 0:
            count += 1
    return count

print(count_odd(listofnum))