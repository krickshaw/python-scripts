#Author krickshaw
# Lectura de un fichero 
# Modos:
# 1) Sólo lectura - Read (r): lo carga en memoria, pero no se puede editar
# 2) Escritura - Write (w): si existe, se borra y se vuelve a escribir. Si no existe lo crea
# 3) Escritura al final (a): escribe a continuación del contenido
# 4) Lectura/Escritura (+): lectura y escritura, pero ojo, porque w+ borra lo que hubiera
file=input("Introduzca fichero:")
mode=input("Introduzca modo de apertura:")

try:
	with open(file, mode) as f:
		if mode.find("r") ==-1:
			write = True
			while  write:
				line=input("Introduzca línea:")
				f.write(line)
				f.write("\n")
				resp=input("¿Terminado (Y/N)?:")
				if resp.upper().find("Y") != -1:
					write = False
					f.close()
					f = open(file,"r")
		print ("El contenido del fichero es el siguiente:")
		contenido = f.read()
		print (contenido)
		f.close()
except:
	print("Error al intentar abrir el fichero")