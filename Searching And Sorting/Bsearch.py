def Bsearch(A,x):
    l = 0
    u = len(A)
    while(l<=u):
        mid = (l+u)//2
        if x == A[mid]:
            return 1
        elif x<A[mid]:
            u = mid-1
        else:
            l = mid+1
    return -1

A = [1,6,7,9,12,23,45,67,81]
x = int(input("Enter the number you want to search for: "))
pos = Bsearch(A,x)
if (pos == -1):
    print("Number not found!!")
else:
    print("Number found at position:",A.index(x))