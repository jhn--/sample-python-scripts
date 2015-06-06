class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg = mpg
	def displayCar(self):
		return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."
	def driveCar(self):
		self.condition = "used"

#myCar = Car("DeLorean", "silver", 88)

class ElectricCar(Car):
    def __init__(self, model, color, mpg, typeOfBattery):
    	self.model = model
        self.color = color
        self.mpg = mpg
        self.typeOfBattery = typeOfBattery

myCar = ElectricCar("a", "red", 4, "molten salt")

print myCar.displayCar()

#myCar.driveCar()
#print myCar.condition
