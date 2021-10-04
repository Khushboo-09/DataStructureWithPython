def BsearchRecursive(A,x,l,u):
    if(u>=l):
        mid = (u+l)//2
        if x==A[mid]:
            return 1
        elif(x<A[mid]):
            BsearchRecursive(A,x,l,mid-1)
        else:
            BsearchRecursive(A,x,mid+1,u)
    else:
        return -1


A = [1,6,7,9,12,23,45,67,81]
x = int(input("Enter the number you want to search for: "))
pos = BsearchRecursive(A,x,0,len(A)-1)
if (pos == -1):
    print("Number not found!!")
else:
    print("Number found at position:",A.index(x))
