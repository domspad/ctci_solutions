

# Chapter 1: Arrays and Strings
# Problem 1: 
"""
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""

################################################################################
################################################################################
################################################################################
# SOLUTIONS

"""
Solution 1 : 

Do all n choose 2 comparisons of characters returning false if any match

Time: 		O(n^2)
Space:		O(1)
"""

def hasNoRepeats(text) :
	"""
	Requires text to be sequence structure
	Returns True if all elements of it are unique
	"""
	n = len(text) 
	for i in range(n-1) :
		for j in range(i+1, n) :
			if text[i] == text[j] :
				return False
	return True

"""
Solution 2 : 

Iterates once through string storing letters in dictionary
if one of the letters is already there, then returns false
(note dictionary lookup is O(1))

Time:		O(n)
Space:		O(n)

"""

def hasNoRepeatsFast(text) :
	"""
	Requires: text to be sequence structure and elements hashable
	Returns: True if all elements of structure are unique
	"""
	letters = dict()
	for letter in text :
		if letter in letters :
			return False
		letters[letter] = 1
	return True

"""
Solution 3 : 

Same as Solution 2 but cleverly uses integer to store letters

Time:		O(n)
Space:		O(1)? (int smaller than dict?)

"""

def hasUniqueChars(text) :
	"""
	Requires: text to be sequence structure and elements lower-case characters
	Returns: True if all elements unique otherwise False
	"""
	checker = 0  #our storage int (each binary digit will be a letter)
	for letter in text :
		# print bin(checker)
		val = ord(letter) - ord('a')	#a = 94, z = 122, so val in range(1,26)
		if (checker & (1 << val)) > 0 :  # checks if that letter in checker already
			return False
		checker |= 1 << val #adds letter to checker 
	return True

################################################################################
################################################################################
################################################################################
# TESTS

def test_hasNoRepeats() :
	examples = dict([('abcdefhij', True),
					('no repeats', False),
					('', True),
					('a', True),
					('aa', False)])
	assert all(hasNoRepeats(ex) == val for ex,val in examples.items())
	assert all(hasNoRepeatsFast(ex) == val for ex,val in examples.items())
	print 'passes tests'


if __name__ == '__main__':
	test_hasNoRepeats()