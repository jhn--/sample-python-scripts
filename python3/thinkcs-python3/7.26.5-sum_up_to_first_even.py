'''
Sum all the elements in a list up to but not including the first even number. (Write your unit tests. What if there is no even number?)
'''

def checkforeven(l):
    for i in l:
        if i % 2 == 0:
            return sum_up_to_first_even(l)
    return None                                 #No even numbers found.

def sum_up_to_first_even(l):
    total = 0
    for i in l:
        if i % 2 == 0:
            break
        total += i
    return total

listofnum = [31, 67, 99, 101, 2, 55, 4]
listofnum2 = [1, 2, 3, 4, 5, 6]
listofnum3 = [1, 11, 111, 1111]
listofnum4 = [2, 3, 4, 5, 6]
listofnum5 = []

print(checkforeven(listofnum))
print(checkforeven(listofnum2))
print(checkforeven(listofnum3))
print(checkforeven(listofnum4))
print(checkforeven(listofnum5))