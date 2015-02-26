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


    #incorporate
#############################
#Divide
#############################

#binary tree python
class BinaryTree:
    def __init__(self, content, left = None, right = None):
        self.content = content
        self.left = left
        self.right = right

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

#Given a sorted (increasing order) array with unique integer elements, write an
#algorithm to create a binary search tree with minimal height.


def int_array_to_binary_search_tree(intarray):
    #use the middle of the array to divide it. this ensures minimal height.
    if len(intarray) == 0:
        return None
    if len(intarray) == 1:
        return BinaryTree(intarray[0])
    cut = len(intarray) / 2
    return BinaryTree( intarray[cut], \
        int_array_to_binary_search_tree(intarray[0:cut]), 
        int_array_to_binary_search_tree(intarray[cut+1:]))

#testing

intarray1=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,144,515]
intarray2=[1,2,3,4,5,6,7,8,9,10,12,15,18,22,43,144,515,4123]

print str(int_array_to_binary_search_tree(intarray1))

print str(int_array_to_binary_search_tree(intarray2))