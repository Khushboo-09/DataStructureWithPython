class _Node:
    __slots__='_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class StackLinkedLIst:
    
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size==0
    
    def push(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._top = newest
        else:
            newest._next= self._top
            self._top = newest
        self._size += 1
    
    def pop(self):
        if self.isempty():
            print("The stack is empty!!! Nothing to Pop.")
            return
        else:
            e = self._top._element
            self._top = self._top._next
        self._size -= 1
        return e 

    def top(self):
        if self.isempty():
            print("The stack is empty!!!! Nothing on the Top.")
            return
        else:
            return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element,end = "  ")
            p = p._next
        print()


s = StackLinkedLIst()
s.push(45)
s.push(78)
s.push(34)
s.display()
print("Top element is : ",s.top())
print("Length of the stack: ",len(s))
print("Popped Element is :", s.pop())
s.display()
print("Top element is : ",s.top())
print("Length of the stack: ",len(s))

