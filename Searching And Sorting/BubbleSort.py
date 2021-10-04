def BubbleSort(A):
    for p in range(len(A)-1):
        for i in range(p):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i]=A[i+1]
                A[i+1] = temp
  
            

A = [23,6,78,1,34,25,56,36]
BubbleSort(A)
print(A)