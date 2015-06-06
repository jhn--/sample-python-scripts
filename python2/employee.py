#!/usr/bin/python

class Employee(object):
	"""Models real-life employees!"""
	def __init__(self, employee_name):
		self.employee_name = employee_name
	
	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
	def __init__(self, employee_name):
		self.employee_name = employee_name

	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 12.00

pt1 = PartTimeEmployee("pt1")

print pt1.calculate_wage(2)

emp1 = Employee("emp1")

print emp1.calculate_wage(2)
