def CountSort(A):
    n = len(A)
    size = max(A)
    carray = [0]*(size+1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i,j = 0,0
    while i < size+1:
        if carray[i]>0:
            A[j] = i
            j+=1
            carray[i] = carray[i]-1
        else:
            i = i+1


    
A = [23,6,78,1,34,25,56,36]
CountSort(A)
print(A)





