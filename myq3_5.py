# O(1) removing but O(n) pushing!
class MyQueue: 

	def __init__(self) :
		self.stacks = [[],[]]

	def show(self) :
		print "stack 0: ","->".join(map(str,self.stacks[0]))
		print "stack 1: ", "->".join(map(str,self.stacks[1]))
		print '\n'

	def empty(self) :
		return self.stacks[0] == []

	def add(self,x) :
		# self.stacks[1-self.current].append(x) 
		while self.stacks[0] != [] :
			self.stacks[1].append(self.stacks[0].pop())
		self.stacks[0].append(x)
		while self.stacks[1] != [] :
			self.stacks[0].append(self.stacks[1].pop())

	def remove(self) :
		if self.empty() :
			raise Exception("empty queue!")
		return self.stacks[0].pop()

def test_myqueue() :
	q = MyQueue()

	for i in range(10) : 
		q.add(i)
		# if i % 3 == 1 :	
			# q.remove()
		q.show()
	for i in range(10) :
		print q.remove()
	q.show()
	print "passes tests"

if __name__ == "__main__" :
	test_myqueue() 