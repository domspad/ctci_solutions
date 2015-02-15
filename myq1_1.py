
def hasNoRepeats(text) :
	"""checks if all unique chars in text with O(1) space O(n^2) time
		(i.e. does all n choose 2 comparisons)"""
	n = len(text) 
	for i in range(n-1) :
		for j in range(i+1, n) :
			if text[i] == text[j] :
				return False
	return True

def hasNoRepeatsFast(text) :
	"""checks if all unique chars in text with O(n) space and time
		(i.e. one pass through string with dict storage (O(1) lookup))"""
	letters = dict()
	for letter in text :
		if letter in letters :
			return False
		letters[letter] = 1
	return True

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