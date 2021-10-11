class _Node:
    __slots__= '_element','_next','_prev'
    def __init__(self,element,next,prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size==0

    def AddLast(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1

    def AddAtBeginning(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head  = newest
        self._size += 1

    def AddAtAny(self,e,pos):
        newest = _Node(e,None,None)
        p = self._head
        i = 1
        while i<pos-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p
        self._size += 1

    def RemoveAtBeginning(self):
        if self.isempty():
            print("The list is empty!!! Nothing to Delete.")
            return
        e = self._head._element
        self._head._next._prev = None
        self._head = self._head._next
        self._size  -= 1
        if self.isempty():
            self._tail = None
        return e
            
    def display(self):
        p = self._head
        while p:
            print(p._element,end = "  ")
            p = p._next
        print()

    def displayRev(self):
        p = self._tail
        while p:
            print(p._element,end = "  ")
            p = p._prev
        print()

d = DoublyLinkedList()
d.AddLast(8)
d.AddLast(2)
d.AddLast(9)
d.AddAtBeginning(4)
d.AddLast(6)
d.AddAtBeginning(7)
d.AddAtAny(5,3)
print("The original List is:")
d.display()
print("The list in reverse order is:")
d.displayRev()
print("The list after removing element from beginning which is:",d.RemoveAtBeginning())
d.display()
print("The list in reverse order:")
d.displayRev()
print("The size of the list is: ",d.__len__())

    
    