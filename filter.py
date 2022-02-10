#Author krickshaw
#Function that filters vowels
def func_vowels(letter):
	vowels = ['a','e','i','o','u']
	if (letter in vowels):
		return True
	else:
		return False

try:
	word = input("Insert a word:")
	filtered = filter(func_vowels,word)

	print('The vowels are:')
	for i in filtered:
		print(i)

except ValueError:
	print("Must insert a valid word")

