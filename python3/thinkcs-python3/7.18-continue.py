'''
using the continue statement
'''

lists = [16, 10, 20, 17, 2, 100]
for i in lists:
    if i % 2 == 1:
        continue
    print(i)
print("done")