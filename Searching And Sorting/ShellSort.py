def ShellSort(A):
    l= len(A)
    gap = l//2
    while(gap>0):
        i = gap
        while(i<l):
            temp = A[i]
            j = i-gap
            while j>=0 and A[j]>temp:
                A[j+gap]= A[j]
                j = j-gap
            A[j+gap] = temp
            i +=1
        gap = gap//2

A = [23,6,78,1,34,25,56,36]
ShellSort(A)
print(A)
