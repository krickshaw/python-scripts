#Author krickshaw
# Comprueba que la contraseña introducida es correcta
import hashlib
import getpass
import os

passwd = getpass.getpass('Introduzca una password:')
encoder = passwd.encode('utf_8')
passwdhashed = hashlib.sha256(encoder).hexdigest()

passwdcheck = getpass.getpass('Comprobación de password:')
encodercheck = passwdcheck.encode('utf-8')
passwdcheckhasehed = hashlib.sha256(encodercheck).hexdigest()


if passwdhashed == passwdcheckhasehed:
	print("Las contraseñas introducidas son iguales: %s / %s" % (passwdhashed, passwdcheckhasehed))
else:
	print("Las contraseñas introducidas son distintas: %s / %s" % (passwdhashed, passwdcheckhasehed))

