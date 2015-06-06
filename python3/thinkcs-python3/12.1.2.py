'''
12.1.2
'''

import random

def make_random_ints(num, lower_bound, upper_bound):

#one thing that bothers me is why is there a need to assign a variable to a class, like "rng = random.Random()"? Actually there isn't, as proven below.
#assigning a variable to a class makes it easier for the programmer to manage the code

    #rng = random.Random()
    result = []
    for i in range(num):
        #result.append(rng.randrange(lower_bound, upper_bound))
        result.append(random.Random().randrange(lower_bound, upper_bound))
    return result

#print(make_random_ints(input("three numbers: ")))
print(make_random_ints(5, 0, 26))

#btw, this set of codes above will create duplicates.
#if duplicates are undesired, go for the set of codes below.
#try entering a seed value of 1 into random.Random(), eg. random.Random(1)
#you'll get [4,4,4,4,4]

def make_unique_random_ints(num, lower_bound, upper_bound):
    rng = random.Random()
    xs = list(range(lower_bound, upper_bound))
    rng.shuffle(xs)
    result = xs[:5] #get the first 5 elements from the array(xs). elements 0 to 4
    return result

print(make_unique_random_ints(5, 0, 26))

#make_unique_random_ints will be a performance disaster if we are picking a small amount of unique numbers from a huge pool. Hence, the below, more resource saving algorithm.

def make_unique_worthwhile_random_ints(num, lower_bound, upper_bound):
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            print("generating candidate...")
            if candidate not in result:
                print("candidate not in result")
                break 
                #break away from the infinite while loop, this is our escape clause. if candidate _is_in_ results[]. the while loop will ensure that it will seek for another number.
                #I admit this is cool, but I'll need to stare at this code a many minutes more to wrap my head around the idea what the while loop does so much with so little instructions.
                #i've added 2 print commands to show instances the while loop carried on seeking for a number that doesn't already exist in result[].
        result.append(candidate)
    return result

print(make_unique_worthwhile_random_ints(5, 0, 20))

#when you are looking for 10 unique integers from a list of 5, the program will hang.

#xs = make_unique_worthwhile_random_ints(10, 1, 6)
#print(xs)