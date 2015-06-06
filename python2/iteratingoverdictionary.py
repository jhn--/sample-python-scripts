print "iterating over dictionaries"
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print movies.items()

print "comprehending comprehensions"
threes_and_fives = [i for i in range(1,16) if i%3==0 or i%5==0]
print threes_and_fives

print "list slicing"
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = [i for i in garbled[::-2]]
message = str(''.join(message))
print message

print "lambda expressions"
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message =  filter(lambda i: i != "X", garbled)
print message