'''
11.4.list_membership

compare it with 7.22
file in 7.22-nested_loops_for_nested_data.py

'''

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

counter = 0
for (name, subjects) in students:
    if "CompSci" in subjects:
        counter += 1

print("The number of students taking CompSci is %d.") % counter

'''
vs 

counter = 0
for (name, subjects) in students:
    for i in subjects:
        if i == "CompSci":
            counter+=1
print(counter, "students are taking CompSci.")
'''
