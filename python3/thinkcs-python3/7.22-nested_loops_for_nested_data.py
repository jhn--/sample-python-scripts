'''
nested loops for nested data
'''

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

#how many subjects are each students taking?
for (name, subjects) in students:
    print(name, "takes", len(subjects),"subjects.")

#how many students are taking CompSci?
counter = 0
for (name, subjects) in students:
    for i in subjects:
        if i == "CompSci":
            counter+=1
print(counter, "students are taking CompSci.")