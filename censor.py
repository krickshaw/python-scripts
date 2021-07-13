#Author krickshaw
import random
import string

# La función censor devuelve el texto con la palabra indicada reemplazada por *
def censor(text, word):
	listWords = text.split()
	listAux = []
	wordAux = ""
	wordReturn = ""

	for i in listWords:
		if i == word:
			wordAux = "*"*len(word)
		else:
			wordAux = i
		listAux.append(wordAux)

	wordReturn = " ".join(listAux)
	return wordReturn

print(censor("this hack is wack hack", "hack"))