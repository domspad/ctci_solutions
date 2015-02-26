#!/usr/bin/env python

def zeroRowsCols(arr, m=None,n=None) :
	"""Modifies 2d list of values by putting zeros in all rows and cols that
	have a 0 in them to begin with"""
	rows = set()	#initialize sets to track rows/cols to zero out
	cols = set()
	if m == None : m = len(arr)
	if n == None : n = len(arr[0])

	for i in range(m) :
		for j in range(n) :
			if arr[i][j] == 0 :   #mark row + col of cell with 0
				rows.add(i)
				cols.add(j)

	for i in range(m) :		# run through array again and zero out marked cols/rows
		for j in range(n) :
			if (i in rows) or (j in cols) : #NOTE: if '!=' instead of 'or' then does xor
				arr[i][j] = 0

def test_zero() :
	a = [[1,1],
		 [1,1],
		 [1,1]]

	b = [[1,0],
		 [1,0],
		 [1,1]]

	zeroRowsCols(a)
	zeroRowsCols(b)

	assert a == [[1,1],
		 			[1,1],
		 			[1,1]]
	assert b == [[0,0],
		 		[0,0],
		 		[1,0]]

	print "passes tests"

if __name__ == '__main__' :
	test_zero()

	#incorporate
#############################
#Divide
#############################