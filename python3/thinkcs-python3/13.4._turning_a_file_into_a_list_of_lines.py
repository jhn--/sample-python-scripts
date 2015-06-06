'''
13.4._turning_a_file_into_a_list_of_lines
'''

f = open("text.txt", "r")
xs = f.readlines()
f.close()

xs.sort()
print(xs)
for i in xs:
    print(i)

g = open("sorted_lines.txt", "w")
for i in xs:
    g.write(i)

g.close()