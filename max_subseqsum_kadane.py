def maxSubSeqfast(arr) :
	max_end_here = 0
	max_so_far = 0
	for i in range(len(arr)) :
		max_end_here = max(0, max_end_here + arr[i])
		max_so_far = max(max_so_far, max_end_here) 
	return max_so_far 


def test_maxSubSeq() :
	# not sure how to handle cases with multiple equal subsums (earlist, shortest?)
	testdict = { (1,2) : 3,
				(1,) : 1,
				(-1,) : 0,
				# (1,1,0,-2) : (0,)
				(-10,5,5,-10) : 10,
				(1,1,-1,0,2,-1,0) : 3}
	assert all(maxSubSeqfast(k) == v for k,v in testdict.items())
	for k,v in testdict.items() :
		print k, 'check',v, '==' ,maxSubSeqfast(k)
	print "passes tests"

if __name__ == '__main__' :
	test_maxSubSeq()