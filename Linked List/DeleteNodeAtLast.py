class _Node:
    __slots__='_element','_next'
    def __init__(self,element,next):
        self._element = element 
        self._next = next


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size ==0

    def addLast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size +=1

    def addBeginning(self,e):
        newest  = _Node(e,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size+=1

    def addAny(self, e,pos):
        newest = _Node(e,None)
        p = self._head
        i = 1
        while i<pos-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size +=1
    
    def DeleteAtBeginning(self):
        if self.isempty():
            print("List is emplty!!! Nothing to delete.")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail._next = None
        return e

    def DeleteAtLast(self):
        if self.isempty():
            print("List is empty!!! Nothing to delete.")
            return
        p = self._head
        i = 1
        while i<self.__len__()-1:
            p = p._next
            i = i + 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1
        return e
        
    def display(self):
        p = self._head
        while p:
            print(p._element,end = "  ")
            p = p._next
        print()
        


l = LinkedList()
l.addBeginning(56)
l.addLast(67)
l.addBeginning(89)
l.addLast(45)
l.addBeginning(65)
l.addLast(23)
l.addBeginning(90)
l.addLast(25)
l.addBeginning(82)
l.addLast(15)
l.display()
print("Size: ",len(l))
l.addAny(40,3)
l.addAny(12,6)
l.display()
print("Size: ",len(l))

print("The element deleted is: ",l.DeleteAtLast())
l.display()
print("Size: ",len(l))