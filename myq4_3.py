class BinaryTree(object) :
	"""No empty trees allowed (empty tree should be represented by None) """
	def __init__(self, val, left=None, right=None) :
		self.val = val
		self.left = left
		self.right = right

	def __str__(self) :
		print str(self.val)
		# print "( {} ( {} | {} ))".format(str(self.val), self.left, self.right)

def fillTree(root, data) :
	n = len(data)
	if n > 0 : 
		root.val = data[n/2]
		root.left = BinaryTree(0)
		root.right = BinaryTree(0)
		fillTree(root.left, data[:n/2])
		fillTree(root.right, data[n/2 + 1:])
	else :
		root = None

emptytree = BinaryTree(0)

array = range(0,7)

fillTree(emptytree, array)
emptytree.__str__()
print array
print emptytree

