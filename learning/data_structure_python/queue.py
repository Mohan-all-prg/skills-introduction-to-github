"""queue=[]
def add():
    if len(queue)==a:
        print("the list is reached the range")
    else:
        b=input("enter the element=")
        queue.append(b)
        print(queue)
def remove():
    if not queue:
        print("give value to get output")
    else:
        print("removed=",queue.pop(0))
        print(queue)

a=int(input("Enter the range="))
while True:
    print("To run the function for add:1 or remove:2 or stop:3")
    c=int(input("Enter="))
    if(c==1):
        add()
    elif(c==2):
        remove()
    elif(c==3):
        break
    else:
        print("UNDEFINED FUNCTION?")"""


"""import collections
a=collections.deque([])
for i in range(3):
    b=input("Enter num=")
    a.appendleft(b) #here we can use popleft 
print(a)"""

import queue
a=queue.Queue()
for i in range(3):
    b=input("Enter num=")
    a.put(b) #here we can remove by using get() keyword
print(a)#it will be an object so it would not show output
print(a.get())


"""a=[(230,245),(1,99),(100,1)]
a.sort(reverse=True)
print(a)"""
















