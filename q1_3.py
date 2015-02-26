
def removeDupCharsCString(text) :
	"['h','e','l','l','o',''] --> ['h','e','l','o','', ...<can be stuff here> ..]"
	check = copy = 0
	letters = set()
	while( text[check] != '') :
		if text[check] in letters :
			check += 1
		else :
			letters.add(text[check])
			text[copy] = text[check] 
			check += 1
			copy += 1
	text[copy] = text[check] #for the null character
	del text[copy+1:]


def test_removeDup() :
	exs = [(list('hello')+[''], list('helo')+['']),
			(list('abccddbbf')+[''], list('abcdf')+['']),
			(list('aaaaaaa')+[''], list('a')+['']),
			(list('abc')+[''], list('abc')+[''])]
	for ex in exs :
		print ex[0]
		removeDupCharsCString(ex[0])
		assert ex[0] == ex[1]
		print ex[0], ' becomes ', ex[1], '\n'
	print "passes tests"

if __name__ == '__main__' :
	test_removeDup()


#incorporate
#############################
#Divide
#############################