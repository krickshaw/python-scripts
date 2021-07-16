#Author krickshaw
# Ejemplo de clase, herencia, variables miembro y métodos de clase padre y que permiten cambiar una variable miembro (setter)
class Car (object):
	condition = "new"

	# Constructor
	def __init__(self, model, colour, mpg):
		self.model = model
		self.colour = colour
		self.mpg = mpg

	# Methods
	def viewCar(self):
		cad = str("This is a car model %s, colour %s which reaches %d MPG." %(self.model, self.colour, self.mpg))
		return cad

	def driveCar(self):
		self.condition = "used"

class ElectricCar(Car):
	# Constructor
	def __init__(self, model, colour, mpg, batttype):
		self.model = model
		self.colour = colour
		self.mpg = mpg
		self.batttype = batttype

	def driveCar(self):
		self.condition = "more or less new"

# Objects creation and invocation
myCar = Car("DeLorean", "Silver", 88)
print(myCar.condition)
print(myCar.model)
myCar.driveCar()
print(myCar.condition)

myCar = ElectricCar("DeLorean","Silver","88","ion")
print(myCar.condition)
myCar.driveCar()
print(myCar.batttype)
print(myCar.condition)