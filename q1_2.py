"""
# Chapter 1: Arrays and Strings
# Problem 2: 

Write code to reverse a C-Style String (e.g. 'abcd' == ['a','b','c','d',''])
"""

################################################################################
################################################################################
################################################################################
# SOLUTIONS

"""
Solution 1 : 

Finds end of string then marches backwards appending letters to a new string

Time: 		O(n)
Space:		O(n)
"""

def reverseCString1(cstr) :
	""" 
	Requires: cstr is a sequence of characters where one character is ''
	Returns: list with characters of cstr reversed (last char is '')
	"""
	length = 0
	while(cstr[length] != '' ) :
		length += 1
	result = []
	for i in range(1,length+1) :
		result.append(cstr[length - i])
	result.append('')
	return result

"""
Solution 2 : 

Iterate through chars of string until end 
Then with two end pointers, swap chars of string until both pointers reach middle

Time: 		O(n)
Space:		O(1)
"""

def reverseCString2(cstr) :
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

################################################################################
################################################################################
################################################################################
# TESTS

def test_reverse1() :
	ex = [([''],['']),
			(['a',''],['a','']),
			(['a','b',''],['b','a',''])]
	assert all(reverseCString1(cstr[0]) == cstr[1] for cstr in ex)
	print 'passes tests'

def test_reverse2() :
	exs = [([''],['']),
			(['a',''],['a','']),
			(['a','b',''],['b','a',''])]
	for ex in exs :
		reverseCString2(ex[0])
		assert ex[0] == ex[1] 
	print 'passes tests'

if __name__ == '__main__' :
	test_reverse1()
	test_reverse2()
