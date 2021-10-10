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
            self._tail =newest
        else:
            newest._next = self._head
            self._tail._next = newest
            self._head = newest
        self._size += 1

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
c.display()
print("The size of the List is: ",c.__len__())

    
       