'''
8.16-string_format
'''
n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||"
        .format(n1,n2,n3,1981))
print("The decimal value {0} converts to hex value {0:x}"
        .format(123456))

letter = """
Dear {0} {2}.
 {0}, I have an interesting money-making proposition for you!
 If you deposit $10 million into my bank account, I can
 double your money ...
"""

print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))

print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",
                                            i**10, "\t", i**20)


layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 15):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))

'''
print multiplication table from 1 to 5"
'''
layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}"
print("{0:^}".format("Multiplication Table"))
#print(layout.format(1,2,3,4,5))
print("{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}".format("i", "i*2", "i*3", "i*4", "i*5"))
for i in range(1,14):
    print(layout.format(i, i*2, i*3, i*4, i*5))