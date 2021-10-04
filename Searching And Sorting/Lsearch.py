def Lsearch(A,x):
    for i,y in enumerate(A):
        if y==x:
            return i

    return -1 


A = [23,56,78,3,45,1]
x = int(input("Enter the number you want to search for: "))
pos = Lsearch(A,x)
if (pos == -1):
    print("Number not found!!")
else:
    print("Number found at position:",pos)