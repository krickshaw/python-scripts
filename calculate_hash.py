#Author krickshaw
# Calcula el hash para un fichero o un texto introducido
import hashlib
import os


try:
	fileortext=input("¿Texto (t) o fichero (f)?:")

	if fileortext=='f':
		filevalid=False

		while filevalid==False:
			file=input("Introduzca fichero:")
		
			if os.path.isfile(file):
				filevalid=True
			else:
				print("Fichero especificado no válido")
		obj=file
	else:
		obj=input("Introduzca texto:")

	
	hashalgorithms = ['md5','sha1','sha224','sha256','sha384','sha512']
	hashvalid=False

	while hashvalid==False:
		hashtype=input("Introduzca algoritmo de hash:")
		hashtype=hashtype.lower()

		if hashtype in hashalgorithms:
			hashvalid=True
		else:
			print("Algoritmo de hash especificado no válido")	

	encoder=obj.encode('utf_8')
	if hashtype=="md5":
		myhash=hashlib.md5(encoder).hexdigest()
	elif hashtype=="sha1":
		myhash=hashlib.sha1(encoder).hexdigest()
	elif hashtype=="sha224":
		myhash=hashlib.sha224(encoder).hexdigest()
	elif hashtype=="sha256":
		myhash=hashlib.sha256(encoder).hexdigest()
	elif hashtype=="sha384":
		myhash=hashlib.sha384(encoder).hexdigest()
	elif hashtype=="sha512":
		myhash=hashlib.sha512(encoder).hexdigest()

	print(myhash)

		
except Exception as exc:
	print("Se ha producido un error:" + exc)


#def md5(text):
#	encoder=text.encode('utf_8')
#	myhash=hashlib.md5(encoder).hexdigest()
#	print(myhash)

#def sha1(text):
#	encoder=text.encode('utf_8')
#	myhash=hashlib.sha1(encoder).hexdigest()
#	print(myhash)
