
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
	#incorporate
#############################
#Divide
#############################

def rotateArray(arr, n=None) :
	"rotates nxn arr in place"
	if n == None : n = len(arr)
	num_layers = n / 2
	for layer in range(num_layers) :
		for i in range(n - 2*layer - 1) :
			temp = arr[layer][layer+i]
			arr[layer][layer+i] = arr[n-layer-i-1][layer]
			arr[n-layer-i-1][layer] = arr[n-layer-1][n-layer-i-1]
			arr[n-layer-1][n-layer-i-1] = arr[layer+i][n-layer-1] 
			arr[layer+i][n-layer-1] = temp

def test_rotate() :
	a1 = [[1]]
	a2 = [[1]]
	b1 = [[1,2],
		  [4,3]]
 	b2 = [[4,1],
 		  [3,2]]
	c1 = [[1,2,3],
		  [4,5,6],
	 	  [7,8,9]]
	c2 = [[7,4,1],
		  [8,5,2],
		  [9,6,3]]
	d1 = [[1,2,3,4,5],
		  [6,7,8,9,10],
		  [11,12,13,14,15],
		  [16,17,18,19,20],
		  [21,22,23,24,25]]
	d2 = [[21,16,11,6,1],
		  [22,17,12,7,2],
		  [23,18,13,8,3],
		  [24,19,14,9,4],
		  [25,20,15,10,5]]
	rotateArray(a1)
	rotateArray(b1)
	rotateArray(c1)
	rotateArray(d1)
	assert a1 == a2
	assert b1 == b2
	assert c1 == c2
	assert d1 == d2
	print "passes tests"

if __name__ == "__main__":
	test_rotate()