print "lambda syntax"
languages = ["HTML", "JavaScript", str("Python"), "Ruby"]
print filter(lambda x: x == 'Python', languages)

squares = [i**2 for i in range(1,11)]

print filter(lambda x: 29<x<71, squares)
