import numpy as np 


def nFactTrailZeros(n) :
	"returns number of trailing 0's in n!"
	k = int(np.log(n) / np.log(5))
	result = 0
	for i in range(1,k+1) :
		result += (n / (5**i))
	return result

def testnFact() : 
	ns = (3,9,15,26,127)
	ns_res = (0,1,3,6,31)
	assert all(nFactTrailZeros(ns[i]) == ns_res[i] for i in range(len(ns)))
	print "passes tests"

if __name__ == '__main__' :
	testnFact()