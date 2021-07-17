#Author krickshaw
def powerhouse(num_base, exponent):
	#result = 2**3
	#print("%d" % result)
	#pow(2,3)
	result = num_base**exponent
	print("%0.2f a la %0.2f potencia es %0.2f." %(num_base, exponent, result))

try:
	base=float(input("Introducza base:"))
	exponente=float(input("Introducza exponente:"))
	powerhouse(base,exponente)
except ValueError:
	print("Debe introducir números")