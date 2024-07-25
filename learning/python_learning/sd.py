"""n=10
a=[]
for i in range(2,11):
    if(n%i==0):
        print("sd",i)
        a.append(i)
print("smallest divisor=",a[0])"""

"""i=0
while(i<5):
    print(i)
    i=i+1

for i in range(1,51):
    if(i%2!=0 and i%3!=0):
        print(i)"""

"""import math
a=0
b=0
for i in range(1,51):
    for j in range(1,51):
        if(math.sqrt(j)==i):
           print(i)
        while(j!=0):
                a=int(j%10)
                b=b+a
                j=int(j//10)
                if(b<10):
                    print(b,end="")
                    print()"""

"""a=9
b=8
print("LCM of a and b")
for i in range(1,a*b+1):
    if(i%a==0 and i%b==0):
        print(i)
        c=(a*b)//i
        print("GCD of a and b",c)
        break"""

"""n=5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()"""
