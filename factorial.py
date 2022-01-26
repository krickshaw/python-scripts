#Author krickshaw
def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

#Ejemplos de llamada e impresión por pantalla
#numero = factorial(4)
#print("El factorial de 4 es: %d" % numero)
#
#print(factorial(4))


try:
	number=int(input("Introducza número:"))
	fact = factorial(number)

	print("El factorial de %d es: %d" % (number,fact))

except ValueError:
	print("Debe introducir números")
