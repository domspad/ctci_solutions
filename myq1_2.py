
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