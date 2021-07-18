#Author krickshaw
def primenumber(number):
	numAux = number - 1
	if number > 1:
		while numAux > 1:
			if number%numAux==0:
				return False
			else:
				numAux = numAux - 1
		else:
			return True
	else: 
		return False				


try:
	number=int(input("Introducza número:"))
	esPrime = primenumber(number)

	if esPrime == True:
		print("El número %d es primo" % number)
	else:
		print("El número %d no es primo" % number)

except ValueError:
	print("Debe introducir números")