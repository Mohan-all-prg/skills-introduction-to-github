n=int(input("num="))
b=[]
mo=int(input("num="))
for i in range(mo):
    a=list(input())
    b.append(a)

c=[]
d=0
for i in range(mo):
    c.append(b[i][d])

e=0
f=n%mo
g=f-1
print("the last pass of the ball to a friend is=",c[g])
        
        

    
        

    
