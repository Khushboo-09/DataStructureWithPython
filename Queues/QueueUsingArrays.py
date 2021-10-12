class QueueArrays:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data)==0
    
    def enqueue(self,e):
        self._data.append(e)
    
    def dequeue(self):
        if self.isempty():
            print("The Queue is empty!!! Nothing to remove.")
            return
        else:
            return self._data.pop(0)

    def first(self):
        if self.isempty():
            print("The Queue is empty!!! Nothing on the first.")
            return
        else:
            return self._data[0]

q = QueueArrays()
q.enqueue(45)
q.enqueue(78)
q.enqueue(34)
print(q._data)
print("First element is : ",q.first())
print("Length of the Queue: ",len(q._data))
print("Dequeued Element is :", q.dequeue())
print(q._data)
print("First element is : ",q.first())
print("Length of the Queue: ",len(q._data))

    