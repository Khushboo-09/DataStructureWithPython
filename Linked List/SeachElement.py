class _Node:
    __slots__='_element',"_next"

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
        return self._size==0
    
    def addLast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element,end = "  ")
            p = p._next
        print()
    
    def SearchElement(self,n):
        p = self._head
        index = 0
        while p:
            if p._element ==n:
                return index
            else:
                p = p._next
                index+=1
        return -1

        

l = LinkedList()
l.addLast(45)
l.addLast(34)
l.addLast(56)
l.addLast(90)
l.addLast(89)
l.addLast(32)
l.display()
print("Size: ",len(l))
n = input("Enter the element you want to search for: ")
x = l.SearchElement(n)
if(x>=0):
    print('Element ',n,' found at index: ',x)
else:
    print("Element not Found!!!!")


