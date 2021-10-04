def RadixSort(A):
    n = len(A)
    digits = len(str(max(A)))
    l = []
    bins = [l]*10
    for i in range(digits):
        for j in range(len(A)):
            e = int((A[j]/pow(10,i))%10)
            if len(bins[e])>0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x])>0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k+1




A = [23,6,78,1,34,25,56,36]
RadixSort(A)
print(A)