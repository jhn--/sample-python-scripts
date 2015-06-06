#! /usr/bin/python

#When teaching a class, it's important to take the students' averages in order
#to assign grades. First, write a function average that takes the average
#value of a list filled only with numbers. If you need help with this, take a
#look at the Hint.

Lloyd = {
    "name":"Lloyd",
    "homework": [90,97,75,92],
    "quizzes": [ 88,40,94],
    "tests": [ 75,90]
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

students = [Lloyd, Alice, Tyler]

def average(scores):
    return (sum(scores)/len(scores))

def getAverage(students):
    whwrk = average(students['homework']) * 0.1
    wqiz = average(students['quizzes']) * 0.3
    wtst = average(students['tests']) * 0.6
    wttl = whwrk + wqiz + wtst
    return wttl
#    return str(wttl) + " " + getLetterGrade(wttl)

def getLetterGrade(score):
    score = round(score)
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def getClassAverage(students):
    y = 0
    for x in students:
        y += getAverage(x)/len(students)
#        newy = y/len(students)
    print str(y) + " " + getLetterGrade(y)
#    newy = y/len(students)
#    print str(newy)

#print getAverage(Lloyd)

#for x in students:
#    print x['name'] + " " + str(getAverage(x))

getClassAverage(students)