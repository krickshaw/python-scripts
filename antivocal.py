#Author krickshaw
def anti_vocal(text):
	cad = "aeiouAEIOU"
	cadAux = ""

	for i in text:
		if i not in cad:
			cadAux = cadAux + i

	return cadAux

text=input("Introducza texto:")
print(anti_vocal(text))