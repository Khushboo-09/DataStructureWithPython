class DEqueArrays:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data)==0
    
    def addFirst(self,e):
        self._data.insert(0,e)

    def addLast(self,e):
        self._data.append(e)
    
    def removeFirst(self):
        if self.isempty():
            print("The Queue is empty!!! Nothing to remove.")
            return
        else:
            return self._data.pop(0)

    def removeLast(self):
        if self.isempty():
            print("The Queue is empty!!! Nothing to remove.")
            return
        else:
            return self._data.pop()

    def first(self):
        if self.isempty():
            print("The Queue is empty!!! Nothing on the first.")
            return
        else:
            return self._data[0]

    def last(self):
        if self.isempty():
            print("The Queue is empty!!! Nothing on the first.")
            return
        else:
            return self._data[-1]

q = DEqueArrays()
q.addFirst(45)
q.addLast(78)
q.addFirst(34)
print(q._data)
print("First element is : ",q.first())
print("Last element is : ",q.last())
print("Length of the DEque: ",len(q._data))
print("Removing from beginning: ", q.removeFirst())
print("Removing from end: ", q.removeLast())
print(q._data)
print("First element is : ",q.first())
print("Length of the DEque: ",len(q._data))

    