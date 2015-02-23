
def lexorder(word) :
	return sorted(word)

def anagramSort(words) :
	"""sorts list of words so anagrams a next to each other
	more specifically, uses lexicographic order on sorted versions of 
	each word"""
	words.sort(key=lexorder)

def test_anagramSort() :
	WORDS = ['ADAM','BEAT','ZACK','MDAA','AMAD','EBTA']
	print WORDS
	anagramSort(WORDS) 
	print WORDS
	assert WORDS == ['ADAM','MDAA','AMAD','BEAT','EBTA','ZACK']
	print "passes tests"


if __name__ == '__main__' :
	test_anagramSort()