#Author krickshaw
# Listado de directorios
import os

try:
	dirvalid=False

	while dirvalid==False:
		path=input("Introduzca directorio:")
	
		if os.path.isdir(path):
			dirvalid=True
		else:
			print("Directorio especificado no válido")

	files = os.listdir(path)
	for file in files:
		print(file)
except Exception as exc:
	print("Se ha producido un error:" & exc)