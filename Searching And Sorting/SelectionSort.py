def selectionSort(A):
    for i in range(len(A)-1):
        position =i
        for j in range(i+1,len(A)):
            if A[j]<A[position]:
                position =j
            temp = A[position]
            A[position] = A[i]
            A[i] = temp

A = [23,6,78,1,34,25,56,36]
selectionSort(A)
print(A)