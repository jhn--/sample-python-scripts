class Fruit(object):
	def __init__(self,name, color,flavor, poisonous):
		self.name = name
		self.color = color
		self.flavor = flavor
		self.poisonous = poisonous

	def description(self):
		print "i am %s %s and i taste %s" % (self.color, self.name, self.flavor)

	def is_edible(self):
		if not self.poisonous:
			print "yep! i am edible."
		else:
			print "dont eat me you will dieeeeee"

lemon = Fruit("lemon","yellow","sour", False)

lemon.description()
lemon.is_edible()