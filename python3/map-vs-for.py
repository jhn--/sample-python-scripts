import itertools

@profile
def multiplyby2(x):
    return x*2

array = [1,2,3,4,5,6,7,8,9,10]

@profile
def mapmap():
    map(multiplyby2, array)

@profile
def domap():
    for i in map(multiplyby2, array):
        print(i)

@profile
def dofoor():
    for i in array:
        print(multiplyby2(i))

@profile
def starmap(multiplyby2, array = array):
    for i in array:
        yield multiplyby2(*i)

mapmap()
domap()
dofoor()
print(starmap())