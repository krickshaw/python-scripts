#Author krickshaw
import random
import string

def crear_pass(n):
	allchars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
	passphrase = []

	for i in range(n):
		tmp = random.choice(allchars)
		passphrase.append(tmp)

	res = "".join(passphrase)
	return res

n = int(input("Longitud de password:"))
test = crear_pass(n)
try:
	print(test)
except:
	print("Debe ingresar Longitud")