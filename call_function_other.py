#Author krickshaw
# Llamadas a scripts

from reverse import reverse	 # De esta forma se importa únicamente la función 
import antivocal as av  # De esta forma se importa el archivo completo

try:
	cadena=input("Introducza una cadena de texto:")
	cadenaInversa = reverse(cadena)
	cadenaSinVoca = av.anti_vocal(cadena)

	print("La inversa de la cadena: %s es: %s" % (cadena, cadenaInversa))
	print("La cadena sin vocales de la cadena: %s es: %s" % (cadena, cadenaSinVoca))

except ValueError:
	print("Debe introducir una cadena válida")