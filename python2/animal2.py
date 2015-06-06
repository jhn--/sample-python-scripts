#!/usr/bin/python

class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Add your method here!
	def description(self):
		print self.name, self.age

hippo = Animal("hip",1)
hippo.description()