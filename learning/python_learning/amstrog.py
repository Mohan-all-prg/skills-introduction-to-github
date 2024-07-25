"""n=input()
b=len(n)
n1=int(n)
m=n1
c=0
d=0
while(n1!=0):
    c=n1%10
    d=d+(c**b)
    n1=n1//10
if(m==d):
    print(d)"""

    
"""n=(input())
b=len(n)
print(b)"""

"""n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        if(j==i or i==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i,n):
        if(j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""

"""n=5
for i in range(n):
    for j in range(i,n):
        if(i==0):
            print(i,end=" ")"""
"""n=5
for i in range(n):
    for j in range(i):
        if(j==0 or i==4 or i==j+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""



n=5
for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print()



    
"""if(i==4 or j==0 or i==j+1):
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()"""





