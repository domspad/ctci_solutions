

def findRotation3(alist) :
	"""assumes sorted and with unique elements
	Returns the index of smallest element"""
	def p(v) :
		return v < alist[0] 
	lo, hi = 0, len(alist) -1
	best_so_far = 0
	while(lo <= hi) :     #stops once search sublist is empty
		m = (lo+hi)/2     #takes floor midpoint
		if p(alist[m]) :
			best_so_far = m  #only sets best_so_far if predicate met
			hi = m - 1        #moves endpoints past midpoint
		else :
			lo = m + 1
	return best_so_far    #best_so_far is the index of smallest element

def test_find3() :
	assert findRotation3([1]) == 0
	assert findRotation3([1,2]) == 0
	assert findRotation3([2,1]) == 1
	assert findRotation3([1,2,3]) == 0
	assert findRotation3([3,1,2]) == 1
	assert findRotation3([2,3,1]) == 2
	assert findRotation3(list(range(10))) == 0
	print "passes tests"


def findRotation2(alist) :
	n = len(alist)
	if alist[0] < alist[-1] :
		return 0
	first = alist[0]
	l, r = 0, n-1
	while( l < r -1 ) :
		# print l,r
		m = (l + r)/2
		if alist[m] > first :
			l = m 
		else :
			r = m 
	return r

def binSearchk2(alist, x, k=0) :
	n = len(alist)
	l, r = 0, n-1
	while( l != r ) :
		m = (l+r) / 2
		if x == alist[m] :
			l = r = m
		elif x > alist[m] :
			l = m + 1
		else :
			r = m
	return l if alist[l] == x else -1


def test_findRotate() :
	tests = [[2,3,4,5,6,1],
		[3,4,5,6,1,2],
		[4,5,6,1,2,3],
		[5,6,1,2,3,4],
		[6,1,2,3,4,5],
		[1,2,3,4,5,6]]
	tests.reverse()
	for e, test in enumerate(tests):
		assert findRotation2(test) == e
	print "passes tests"

def test_binSearch() :
	alist = range(20)
	for i in range(20) :
		assert binSearchk2(alist, i) == i
	assert binSearchk2(alist,20) == -1

# """TRACK ENDPOINTS INSTEAD! (broken)"""
def findRotation(alist) :
	"""returns amount sorted list has been rotated by
	requires alist to not be empty"""
	n = len(alist)
	first = alist[0]
	i = n/2
	jump = n/4
	while(jump > 0) :
		print 'i is', i, 'jump is', jump
		i = i + jump if alist[i] > first else i - jump
		jump /= 2
	if first < alist[i] :
		i = 0
	return i

def binSearchk(alist, x, k=0) :
	"""does binary search for x in alist with rotation k"""
	n = len(alist)
	mid = (k+ n/2) % n
	jump = n/4
	while(jump > 0) :
		if alist[mid] == x :
			return mid
		mid = (mid+jump)%n if alist[mid] < x else (mid-jump)%n
		jump /= 2
	return -1



def test_searchRotation() :
	alist = [6,7,8,1,2,3,4,5]
	blist = range(1,9)
	clist = [2,3,4,5,6,7,8,1]
	tricky = [1,2,3,4,5,6,7,8,1]
	# assert findRotation(alist) == 3
	# assert findRotation(blist) == 0
	print findRotation(tricky)
	print findRotation(clist)	

if __name__ == '__main__' :
	# test_searchRotation()
	test_findRotate()
	test_binSearch()
	test_find3()