"""n=5
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i):
        if(j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i+1):
        if(j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""
n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        if(j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i,n-1):
        print(n, end=" n\n\n")
        print(n-1, end=" n-1\n\n")
        print(n-2,end=" n-2\n\n")
        print("$$$$$$$")
        if(j==(n-2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    """i=0 and n=5
    j=0 and i=0
    j=0 i,n=0,1,2.3,4
    j==i print *
    j=0,i=0,1,2,3 n=4
    j=0 n=2 space'
    j=1,i=1,n=2 space'
    j=2,i=2,n=2 *
    j=3,i=3,n=2 space'"""



    
