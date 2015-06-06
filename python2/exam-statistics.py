import math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
	for grade in grades:
		print grade

#the average grade
def grades_sum(grades):
	total = 0
	for grade in grades:
		total += grade
	return total

#grades_sum(grades)

def grades_average(grades):
	average = 0
#	it is not possible to do this :
#	average = grades_sum(grades) / len(grades)
#	call functions within the function, dont pass the function through as a variable
	sumgrades = grades_sum(grades)
	average = sumgrades / len(grades)
	return average

#print grades_average(grades)
average = grades_average(grades)

def grades_variance(grades, average):
	variance = 0
	for i in grades:
		difference = ((average - i) ** 2)
		variance += difference
	variance /= len(grades)
	return variance

#print grades_variance(grades, average)

variance = grades_variance(grades,average)

def grades_std_deviation(variance):
	stddev = math.sqrt(variance)
	return stddev

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades,average)
print grades_std_deviation(variance)