#Author krickshaw
# Hundir la flota
import random

tablero = []

for x in range(0,5):
	tablero.append(["O"]*5)

def print_tablero(tablero):
	for fila in tablero:
		print(" ".join(fila))
	#cadena = " ".join(fila)
	#print("%s" % (cadena))

print("Let's play battleship")
print_tablero(tablero)


def fila_aleatoria(tablero):
	return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
	return random.randint(0,len(tablero[0])-1)


barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)

#print(barco_fila)
#print(barco_col)

for turno in range(4):
	adivina_fila = int(input("Adivina fila:"))
	adivina_columna = int(input("Adivina columna:"))

	if adivina_fila == barco_fila and adivina_columna == barco_col:
		print("Felicidades, hundiste mi barco")
		tablero[adivina_fila][adivina_columna] = "-"
		print_tablero(tablero)
		break
	else:
		if(adivina_fila<0 or adivina_fila>4) or (adivina_columna<0 or adivina_columna >4):
			print("Te saliste del océano")
		elif(tablero[adivina_fila][adivina_columna]=="X"):
			print("Coordenadas ya bombardeadas")
		else:
			print("Agua!")
			tablero[adivina_fila][adivina_columna] = "X"

	print(turno + 1)
	print_tablero(tablero)

	if turno == 3:
		print("Terminó la partida")	
