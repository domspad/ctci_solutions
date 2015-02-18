
def maxSubSeq(arr) :
	"""Returns start, end indices of subarray with
	 largest sum in array"""
	n = len(arr)
	def subsum(ind) : return sum(arr[ind[0]:ind[1]])
	return max(((i,j) for i in range(n) for j in range(i,n+1)), key=subsum)

def test_maxSubSeq() :
	# not sure how to handle cases with multiple equal subsums (earlist, shortest?)
	testdict = { (1,2) : (0,2),
				(1,) : (0,1),
				(-1,) : (0,0),
				# (1,1,0,-2) : (0,)
				(-10,5,5,-10) : (1,3),
				(1,1,-1,0,2,-1,0) : (0,5)}
	assert all(maxSubSeq(k) == v for k,v in testdict.items())
	for k,v in testdict.items() :
		print k, 'check',v, '==' ,maxSubSeq(k)
	print "passes tests"

if __name__ == '__main__' :
	test_maxSubSeq()
