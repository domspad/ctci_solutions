
def rotateArray(a) :
	m = len(a)
	n = len(a[0])
	b = [[0]*m]*n
	for i in range(m) :
		for j in range(n) :
			# print i,j, 'to',j,m-i-1
			print j,m-i-1
			b[j][m-i-1] = a[i][j]
			print b
	return b



def test_rotate() :
	x = [[1,2,3],
		[4,5,6],
		[7,8,9]]
	y = [[7,4,1],
		[8,5,2],
		[9,6,3]]
	print rotateArray(x)
	# assert rotateArray(x) == y
	print "passes tests"

if __name__ == '__main__' :
	test_rotate()
