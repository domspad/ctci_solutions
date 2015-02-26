
def sortInto(A,B) :
	"""Requires: A, B aleady sorted arrays and A has large end buffer to hold B
				also A, B need at least one element
	   Modifies: A by sorting B into it 
	"""
	a = -1
	while(A[a+1] != None) : #find last element of A
		a += 1
	b = len(B) - 1
	f = a + len(B)
	while(a != -1) :
		if b == -1 : #B is completely sorted into A, nothing else needed
			return
		if A[a] >= B[b] :
			A[f] = A[a]
			a -= 1
		else :
			A[f] = B[b]
			b -= 1
		f -= 1
	while(b != -1) :
		A[f] = B[b]
		b -= 1
		f -= 1


def test_sortInto() :
	A = [4, 5, 6, None, None, None] 
	B = [1,2,3]

	sortInto(A,B)
	print A
	assert A == range(1,7)

	A = [1,None,None ]
	B = [2,3]

	sortInto(A,B)
	assert A == range(1,4)

	print "passes tests"

if __name__ == '__main__' :
	test_sortInto()

	    #incorporate
#############################
#Divide
#############################