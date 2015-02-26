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

    def removeDuplicates(self) :
        """Modifies list to remove all duplicate nodes (keeps first instance)"""
        elements = set()
        nextNode = self.head
        if nextNode != None :
            elements.add(nextNode.data)
            while(nextNode.next != None) :
                if nextNode.next.data in elements :
                    nextNode.next = nextNode.next.next
                else :
                    elements.add(nextNode.next.data)
                    nextNode = nextNode.next

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


def test_removeDup() :
    empty = SingleList()
    
    one = SingleList()
    one.append(1)

    twoUnique = SingleList()
    twoUnique.append(1)
    twoUnique.append(2)

    nonContig = SingleList()
    nonContig.append(1) 
    nonContig.append(2)
    nonContig.append(1)
    nonContig.append(2)
    nonContig.append(3)
    nonContig.append(1)
    nonContig.append(4)

    assert empty.compList([])
    assert one.compList([1])
    assert twoUnique.compList([1,2])
    assert nonContig.compList([1,2,1,2,3,1,4])

    empty.show()
    one.show()
    twoUnique.show()
    nonContig.show()

    empty.removeDuplicates()
    one.removeDuplicates()
    twoUnique.removeDuplicates()
    nonContig.removeDuplicates()

    assert empty.compList([])
    assert one.compList([1])
    assert twoUnique.compList([1,2])
    assert nonContig.compList([1,2,3,4])

    empty.show()
    one.show()
    twoUnique.show()
    nonContig.show()

    print "passes tests"

if __name__ == '__main__' :
    test_removeDup()

    #incorporate
#############################
#Divide
#############################

