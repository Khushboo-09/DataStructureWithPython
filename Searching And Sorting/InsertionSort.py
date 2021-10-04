def InsertionSort(A):   
    for i in range(1,len(A)):
        position = i
        cvalue = A[i]
        while position > 0 and A[position-1] > cvalue:
            A[position] = A[position-1]
            position = position -1
        A[position] = cvalue
 

A = [23,6,78,1,34,25,56,36]
InsertionSort(A)
print(A)