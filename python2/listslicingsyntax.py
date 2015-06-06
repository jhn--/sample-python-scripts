l = [i for i in "abcdefg"]
#['a', 'b', 'c', 'd', 'e', 'f', 'g']
print l[1:7:2]
#['b', 'd', 'f']

l = [i**2 for i in range(1,11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]
#[9, 25, 49, 81]


print "omitting indices"
my_list = range(1,11) # List of numbers 1 - 10
x = len(my_list)
# Add your code below!
print my_list
print x
print my_list[::2]

print "reversing a list"

my_list = range(1,11)
# Add your code below!
backwards = [i for i in my_list[::-1]]
print backwards

print "stride length"

to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = [i for i in to_one_hundred[::-10]]
print backwards_by_tens

print "practice makes perfect"
to_21 = range(1,22)
print to_21
odds = [i for i in to_21 if i%2!=0]
print odds
#middle_third = [i for i in to_21[7:14:1]]
middle_third = [i for i in to_21[third:third*2]]
print middle_third