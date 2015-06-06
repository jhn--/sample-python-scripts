#! /usr/bin/python

#Lloyd = {"name" : "Lloyd", "homework" : [], "quizzes" : [], "tests" : []}
#Alice = {"name" : "Alice", "homework" : [], "quizzes" : [], "tests" : []}
#Tyler = {"name" : "Tyler", "homework" : [], "quizzes" : [], "tests" : []}

#this line is wrong, qn is asking for list, not dictionary. misread T_T
#students = {"Lloyd", "Alice", "Tyler"}

Lloyd = {
    "name":"Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
    }
Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }
Tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }

#the list, students, must be declared below the dictionaries
#if it is declared before the dictionaries, the following errors will occur.
#Traceback (most recent call last):
#  File "./student-becomes-the-teacher-lesson-number-one.py", line 8, in <module>
#    students = [Lloyd, Alice, Tyler]
#NameError: name 'Lloyd' is not defined 
#as you can see, when the list is placed above the dictionaries, the entities of the list becomes undeclared

students = [Lloyd, Alice, Tyler]

for a in students:
	print a['name']
	print a['homework']
	print a['quizzes']
	print a['tests']