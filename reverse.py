#Author krickshaw
def reverse(text):
	inverse = []
	inverseAux = ""

	# El primer argumento de range es dónde empiezas, en este caso en el último carácter de la cadena
	# El segundo es donde terminas, en el -1
	# El tercero, como te vas desplazando
	for i in range(len(text)-1,-1,-1):
		inverse.append(text[i])

	for i in inverse:
		inverseAux = inverseAux + i

	return inverseAux				


try:
	cadena=input("Introducza una cadena de texto:")
	cadenaInversa = reverse(cadena)

	print("La inversa de la cadena: %s es: %s" % (cadena, cadenaInversa))

except ValueError:
	print("Debe introducir una cadena válida")