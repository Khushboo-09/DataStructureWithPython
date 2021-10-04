def MergeSort(A,left,right):
    l = len(A)
    if left<right:
        mid = (left + right)//2
        MergeSort(A,left,mid)
        MergeSort(A,mid+1,right)
        Merge(A,left,mid,right)

def Merge(A,left,mid,right):
    i = left 
    j = mid+1
    k = left
    B = [0]*(right+1)
    while i<=mid and j<=right:
        if A[i]<A[j]:
            B[k] = A[i]
            i = i+1
        else:
            B[k] = A[j]
            j = j+1
        k = k+1
    while i <= mid:
        B[k] = A[i]
        i=i+1
        k = k+1
    while j <= right:
        B[k]=A[j]
        j = j+1
        k = k+1
    
    for x in range(left,right+1):
        A[x] = B[x]

    
A = [23,6,78,1,34,25,56,36]
MergeSort(A,0,len(A)-1)
print(A)