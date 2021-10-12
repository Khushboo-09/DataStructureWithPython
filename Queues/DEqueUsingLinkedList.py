class _Node:
    __slots__='_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next

class DEqueLinkedList:
    def __init__(self):
        self._front = None
        self._rear  = None
        self._size = 0
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size==0

    def addFirst(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1
    
    def addLast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1
    
    def removeFirst(self):
        if self.isempty():
            print("The DEque id empty!!! Nothing to remove")
            return
        e = self._front._element
        self._front = self._front._next
        self._size -+ 1
        return e

    def removeLast(self):
        if self.isempty():
            print("The DEque id empty!!! Nothing to remove")
            return
        e = self._rear._element
        p = self._front
        i = 1
        while i < len(self)-1:
            p = p._next
            i += 1
        self._rear = p
        self._size -= 1
        return e

    def first(self):
        if self.isempty():
            print("The DEque is empty!!!")
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print("The DEque is empty!!!")
            return
        return self._rear._element

    def display(self):
        p = self._front
        while p:
            print(p._element,end = "  ")
            p = p._next
        print()

d = DEqueLinkedList()
d.addFirst(34)
d.addFirst(90)
d.addLast(87)
d.addLast(65)
d.addLast(26)
d.display()
print("First element is : ",d.first())
print("Last element is : ",d.last())
print("Length of the DEque: ",len(d))
print("First element removed :", d.removeFirst())
d.display()
print("First element is : ",d.first())
print("Last element is : ",d.last())
print("Length of the DEque: ",len(d))
print("Last element removed :", d.removeLast())
d.display()
print("First element is : ",d.first())
print("Last element is : ",d.last())
print("Length of the DEque: ",len(d))


