def QuickSort(A,low,high):
    if low<high:
        pi = partition(A,low,high)
        QuickSort(A,low,pi-1)
        QuickSort(A,pi+1,high)

def partition(A,low,high):
    pivot = A[low]
    i = low+1
    j = high
    while  True:
        while i<=j and A[i]<=pivot:
            i = i+1
        while i<=j and A[j]>pivot:
            j = j-1
        if i<=j:
            A[i],A[j] = A[j],A[i]
        else:
            break
    
    A[low],A[j] = A[j],A[low]
    return j
  
A = [23,6,78,1,34,25,56,36]
QuickSort(A,0,len(A)-1)
print(A)