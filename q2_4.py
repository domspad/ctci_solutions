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

    def sumLists(self, other) :
        """Requires lengths of self and other >= 1,
        Returns a linked list representing their sum"""
        if self.head == None or other.head == None :
            raise "doesn't accept empty lists"
        d1 = self.head
        d2 = other.head
        sum = SingleList()
        carry = 0
        while(d1 != None or d2 != None) :
            n1 = 0 if d1 == None else d1.data
            n2 = 0 if d2 == None else d2.data
            t = n1 + n2 + carry
            sum.append(t % 10)
            carry = t / 10
            if d1 != None :
                d1 = d1.next
            if d2 != None :
                d2  = d2.next
        if carry > 0 :
            sum.append(carry)
        return sum


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

def test_sumLists() :
    ex1a = SingleList()
    ex1b = SingleList()
    ex2a = SingleList()
    ex2b = SingleList()
    ex3a = SingleList()
    ex3b = SingleList()

    ex1a.append(9)
    ex1a.append(9)
    ex1a.append(9)
    ex1b.append(2)
    ex1a.sumLists(ex1b).show()
    assert ex1a.sumLists(ex1b).compList([1,0,0,1])

    ex2a.append(1)
    ex2a.append(2)
    ex2a.append(3)
    ex2b.append(6)
    ex2b.append(7)
    assert ex2a.sumLists(ex2b).compList([7,9,3])
    assert ex2b.sumLists(ex2a).compList([7,9,3])

    ex3a.append(9)
    ex3a.append(4)
    ex3b.append(9)
    ex3b.append(4)
    assert ex3a.sumLists(ex3b).compList([8,9])

    print "passes tests"

if __name__ == '__main__' :
    test_sumLists()

    #incorporate
#############################
#Divide
#############################

class Node(object):
 
    def __init__(self, data, next=None):
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

def sumList_recurse(s1,s2,carry=0) :
    """returns sum of s1 and s2 as linked list,
     and is implemented recursively"""
    if s1 == None and s2 == None : 
        return None if carry == 0 else Node(carry)
    result = Node(carry)
    value = carry

    if s1 != None : value += s1.data
    if s2 != None : value += s2.data
    result.data = value % 10

    more = sumList_recurse(None if s1 == None else s1.next,
                            None if s2 == None else s2.next,
                            1 if value > 9 else 0)
    result.next = more
    return result

def sumList(s1,s2) :
    s1 = s1.head
    s2 = s2.head
    result = SingleList()
    result.head = sumList_recurse(s1,s2)
    return result

def test_sumLists() :
    ex1a = SingleList()
    ex1b = SingleList()
    ex2a = SingleList()
    ex2b = SingleList()
    ex3a = SingleList()
    ex3b = SingleList()

    ex1a.append(9)
    ex1a.append(9)
    ex1a.append(9)
    ex1b.append(2)
    assert sumList(ex1a,ex1b).compList([1,0,0,1])

    ex2a.append(1)
    ex2a.append(2)
    ex2a.append(3)
    ex2b.append(6)
    ex2b.append(7)
    sumList(ex2a,ex2b).show()
    assert sumList(ex2a,ex2b).compList([7,9,3])
    assert sumList(ex2b,ex2a).compList([7,9,3])

    ex3a.append(9)
    ex3a.append(4)
    ex3b.append(9)
    ex3b.append(4)
    assert sumList(ex3a,ex3b).compList([8,9])

    print "passes tests"

if __name__ == '__main__' :
    test_sumLists()