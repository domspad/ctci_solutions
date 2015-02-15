
def reverseCString(cstr) :
	start = 0
	end = 0
	# find end
	while(cstr[end] != '') :
		end += 1
	# step back one
	end -= 1
	# swap letters 
	while(end > start) :
		cstr[start], cstr[end] = cstr[end], cstr[start]
		start += 1
		end -= 1

def test_reverse() :
	exs = [([''],['']),
			(['a',''],['a','']),
			(['a','b',''],['b','a',''])]
	for ex in exs :
		reverseCString(ex[0])
		assert ex[0] == ex[1] 
	print 'passes tests'

if __name__ == '__main__' :
	test_reverse()
