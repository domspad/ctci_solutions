def bruteRowSearch(sarray, x) :
	"""searches for x in sarray by iterating through rows and
	performing binary search on each"""
	for row in range(len(sarray)) :
		col = binSearch(sarray[row], x) 
		if col != -1 :
			return row, col
	return False

def binSearch(alist, x) :
	"""performs binary search on alist, returning
	earliest occurence of x (index),
	otherwise returns -1"""
	lo, hi = 0, len(alist)-1
	while(lo<hi) : #invariant: alist[lo] < x and alist[hi] >= x
		m = (lo+hi)/2
		if alist[m] >= x :
			hi = m
		else :
			lo = m+1
	# now either lo == hi or lo > hi
	if lo == hi and alist[lo] == x :
		return lo
	return -1

def test_search():
	sarray = [[1,2,4,8,16],
				[3,5,7,9,17],
				[6,10,11,13,19],
				[9,18,27,30,31]]
	assert bruteRowSearch(sarray,10) == (2,1)
	assert bruteRowSearch(sarray,0) == False
	assert bruteRowSearch(sarray,31) == (3,4)
	print "passes tests"

if __name__ == "__main__":
	test_search()

    #incorporate
#############################
#Divide
#############################