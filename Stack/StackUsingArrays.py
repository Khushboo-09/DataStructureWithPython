class StackArray:
    
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print("The stack is empty!!! Nothing to Pop.")
            return
        else:
            return self._data.pop()
    
    def top(self):
        if self.isempty():
            print("The stack is empty!!! Nothing on the Top.")
            return
        else:
            return self._data[-1]

s = StackArray()
s.push(67)
s.push(23)
print(s._data)
print("Length: ",len(s))
print(s.pop())
print("Is the stack empty? -",s.isempty())
s.push(3)
s.push(28)
s.push(12)
print(s._data)
print("Is the stack empty? -",s.isempty())


