	#incorporate
#############################
#Divide
#############################

def sortWithStack(stack, reverse=False) :
	"sorts stack (increasing) using another stack"
	tmpstack = []
	while(stack != []) :
		tmp = stack.pop()
		while(tmpstack != [] and ((tmpstack[-1] < tmp) != reverse)) :
			stack.append(tmpstack.pop())
		tmpstack.append(tmp)
	while(tmpstack != []) :
		stack.append(tmpstack.pop())

def test_sort() :
	ex = [0,5,4,2,1,3]
	sortWithStack(ex)
	assert ex == range(6)
	sortWithStack(ex,True)
	assert ex == range(5,-1,-1)
	print "passes tests"

if __name__ == '__main__' :
	test_sort()