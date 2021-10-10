class _Node:
    __solts__='_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next

class CirculerLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0

    def AddLast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size +=1

    def AddAtBeginning(self,e):
        newest = _Node(e,None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
            self._head = newest
        self._size += 1

    def AddAtAny(self,e,pos):
        newest = _Node(e,None)
        p = self._head
        i = 1
        while i<pos-1:
            p = p._next
            i = i+1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def DeleteAtBeginning(self):
        if self.isempty():
            print("Nothing to delete!!! The list is empty.")
            return
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._tail._next
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None
        return e

    def DeleteAtLast(self):
        if self.isempty():
            print("Nothing to delete!!! The list is empty.")
            return
        p = self._head
        i = 1
        while i< len(self)-1:
            p = p._next
            i += 1
        e = self._tail._element
        self._tail = p
        p = p._next
        self._tail._next = self._head
        self._size -= 1
        if self.isempty():
            self._head = None
            self._tail = None
        return e
    def DeleteAtAny(self,pos):
        if self.isempty():
            print("Nothing to delete!!! The list is empty.")
            return
        p = self._head
        i = 1
        while i< pos-1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next 
        self._size -= 1
        return e

    
    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element,end = "  ")
            p = p._next
            i = i+1
        print()

c = CirculerLinkedList()
c.AddLast(8)
c.AddLast(3)
c.AddLast(6)
c.AddLast(9)
c.AddAtBeginning(7)
c.AddLast(10)
c.AddLast(2)
c.AddAtAny(23,4)
print("The original List")
c.display()
print("The element Deleted at the beginning is: ",c.DeleteAtAny(5))
c.display()
print("The size of the List is: ",c.__len__())

    
       