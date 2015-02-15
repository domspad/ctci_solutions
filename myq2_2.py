class Node(object):
 
    def __init__(self, data, next):
        self.data = data
        self.next = next
 
 
class SingleList(object):
 
    head = None
    tail = None
 
    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None
 
    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node_value):
        "Removes all instances of node_value, and doesn't say if not there"
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
 
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next

    def nthToLast(self, n) :
        """Returns nth to last element (note n == 1 is last element)
        Requires n >= 1 and length of list to be >= n
        """
        if n == 0 :
            raise Exception("n can't be less than 1")
        runner = self.head
        for i in range(n) :
            try :
                runner = runner.next
            except :
                print "list length < n"
        nth = self.head
        while(runner != None) :
            runner = runner.next
            nth = nth.next
        return nth.data

    def compList(self,complist) :
        """compare data in self to list, returns true if same data in same sequence"""
        n = len(complist)
        current = self.head
        for i in range(n) :
            if current == None or current.data != complist[i] : #current vals same and list not longer
                return False
            current = current.next
        if current != None : #self not longer
            return False 
        return True

def test_nthToLast() :
    normal = SingleList()

    for i in range(9) :
        normal.append(i) 

    try :
        normal.nthToLast(0)
    except :
        print "caught error"

    normal.nthToLast(10)
    assert normal.nthToLast(1) == 8
    assert normal.nthToLast(9) == 0
    assert normal.nthToLast(5) == 4

    print "passes tests"

if __name__ == '__main__' :
    test_nthToLast()








