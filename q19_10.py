import random as rd

dic = { (1,1) : 1,
		(1,2) : 1,
		(1,3) : 1,
		(1,4) : 2,
		(1,5) : 2,
		(2,1) : 2,
		(2,2) : 3,
		(2,3) : 3, 
		(2,4) : 3,
		(2,5) : 4, 
		(3,1) : 4, 
		(3,2) : 4,
		(3,3) : 5, 
		(3,4) : 5, 
		(3,5) : 5,
		(4,1) : 6,
		(4,2) : 6,
		(4,3) : 6,
		(4,4) : 7,
		(4,5) : 7,
		(5,1) : 7 }

def rand5() :
	return rd.randint(1,5)

def rand7() :
	"returns random int in [1,7] using rand5()"
	(a,b) = rand5(), rand5()
	while (a,b) > (5,1) :
		(a,b) = rand5(), rand5()
	return dic[(a,b)]

def testRand7() : 
	res = [0]*7
	Num = 10000.0
	for i in range(int(Num)) :
		res[rand7()-1] += 1
	for x in res:
		print x / Num

if __name__ == '__main__' :
	testRand7() 