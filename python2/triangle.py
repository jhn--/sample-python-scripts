class Triangle(object):
	number_of_sides = 3
	def __init__(self, angle1, angle2, angle3):
		self.angle1 = angle1
		self.angle2 = angle2
		self.angle3 = angle3

	def check_angles(self):
		if self.angle1 + self.angle2 + self.angle3 == 180:
			return True
		else:
			return False

'''	
#this is wrong code
	def check_angles(self, angle1, angel2, angle4):
		if(self.angle1 + self.angle2 + self.angle3) == 180:
			return True
		else:
			return False

a = Triangle(60,60,60)
print a.check_angles(60,60,60)
'''	

#a = Triangle(60,60,60)
#print a.check_angles()

class Equilateral(Triangle):
	angle = 60
	def __init__(self):
		self.angle1 = self.angle
		self.angle2 = self.angle
		self.angle3 = self.angle

a = Equilateral()

print a.check_angles()