
def hasUniqueChars(text) :
	"checks with only an int as extra storage!"
	checker = 0  #our storage int (each binary digit will be a letter)
	for letter in text :
		# print bin(checker)
		val = ord(letter) - ord('a')	#a = 94, z = 122, so val in range(1,26)
		if (checker & (1 << val)) > 0 :  # checks if that letter in checker already
			return False
		checker |= 1 << val #adds letter to checker 
	return True