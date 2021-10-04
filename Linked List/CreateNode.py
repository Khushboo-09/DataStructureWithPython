class _Node:
    __slots__='_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

n1 = _Node(7,None)
n2 = _Node(12,None)
n1._next = n2
