

def anagram_check(text1, text2) :
	letter_counts = [0]*256
	for c in text1 :
		if c != ' ' :
			letter_counts[ord(str.lower(c))] += 1
	for c in text2 : 
		if c != ' ' :
			letter_counts[ord(str.lower(c))] -= 1
	for L in letter_counts :
		if L != 0 :
			return False
	return True

def test_anagram() :
	exs = [('hello', 'o hell', True),
			('abc', 'ABC', True), 
			('', '', True), 
			('I am done', 'made ion', True),
			('abcc', 'cba', False),
			('abc123', '321abc', True)]
	for ex in exs :
		assert anagram_check(ex[0], ex[1]) == ex[2]
	print "passes tests"

if __name__ == '__main__' :
	test_anagram()