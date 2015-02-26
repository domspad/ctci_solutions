

def reverseCString1(cstr) :
	# not in place
	""" ex: cstr == ['h', 'e', 'l','l','o',''], and len() is not O(1) """
	length = 0
	while(cstr[length] != '' ) :
		length += 1
	result = []
	for i in range(1,length+1) :
		result.append(cstr[length - i])
	result.append('')
	return result

# def reverseCString2(cstr) :
# 	""" ex: cstr == ['h', 'e', 'l','l','o',''], and len() is not O(1) """
# 	# in place?
# 	length = 0
# 	while(cstr[length] != '' ) :
# 		length += 1
# 	result = []
# 	for i in range(length) :
# 		result.append(cstr[length - i])
# 	return result


def test_reverse() :
	ex = [([''],['']),
			(['a',''],['a','']),
			(['a','b',''],['b','a',''])]
	assert all(reverseCString1(cstr[0]) == cstr[1] for cstr in ex)
	print 'passes tests'

if __name__ == '__main__' :
	test_reverse()

#incorporate
#############################
#Divide
#############################

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
