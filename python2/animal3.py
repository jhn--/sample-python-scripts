#!/usr/bin/python

class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	health = "good"
	def __init__(self, name, age):
		self.name = name
		self.age = age

sloth = Animal("sloth",1)
ocelot = Animal("ocelot",2)

print sloth.health
print ocelot.health
